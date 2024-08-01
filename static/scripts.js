document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const searchForm = document.getElementById('searchForm');
    const attendeeList = document.getElementById('attendeeList');
    const checkedInList = document.getElementById('checkedInList');
    const guestDetails = document.getElementById('guestDetails');
    const uploadMessage = document.getElementById('uploadMessage');
    const menuSelect = document.getElementById('menuSelect');
    const attendanceStats = document.getElementById('attendanceStats');
    const clock = document.getElementById('clock');
    const countdown = document.getElementById('countdown');
    const undoButton = document.getElementById('undoButton');
    const loadedFile = document.getElementById('loadedFile');
    const saveButton = document.getElementById('saveButton'); // Ensure this line is present

    let backupTimer = 60; // 60 seconds countdown for backup
    let lastAction = null;

    const updateClock = () => {
        const now = new Date();
        clock.textContent = now.toLocaleTimeString();
    };

    const updateCountdown = () => {
        countdown.textContent = `Next backup in: ${backupTimer}s`;
        if (backupTimer > 0) {
            backupTimer--;
            setTimeout(updateCountdown, 1000);
        } else {
            backupTimer = 60;
            setTimeout(updateCountdown, 1000);
        }
    };

    const updateAttendeeList = (data) => {
        attendeeList.innerHTML = '';
        data.forEach(attendee => {
            const attendeeDiv = document.createElement('div');
            attendeeDiv.innerHTML = `
                <p>Name: ${attendee.name}</p>
                <p>Email: ${attendee.email}</p>
                <p>ID: ${attendee.id}</p>
                <p>Checked In: ${attendee.checked_in ? 'Yes' : 'No'}</p>
                <p>Check-in Time: ${attendee.check_in_time || 'N/A'}</p>
                <hr>
            `;
            attendeeList.appendChild(attendeeDiv);
        });
    };

    const updateCheckedInList = (data) => {
        checkedInList.innerHTML = '';
        data.forEach(attendee => {
            const attendeeDiv = document.createElement('div');
            attendeeDiv.innerHTML = `
                <p>Name: ${attendee.name}</p>
                <p>Email: ${attendee.email}</p>
                <p>ID: ${attendee.id}</p>
                <p>Checked In: Yes</p>
                <p>Check-in Time: ${attendee.check_in_time}</p>
                <hr>
            `;
            checkedInList.appendChild(attendeeDiv);
        });
    };

    const updateGuestDetails = (data) => {
        guestDetails.innerHTML = '';
        data.forEach(guest => {
            const guestDiv = document.createElement('div');
            guestDiv.innerHTML = `
                <p>Name: ${guest.name}</p>
                <label><input type="checkbox" class="check-in-checkbox" data-name="${guest.name}" ${guest.checked_in ? 'checked' : ''}> Check-in</label>
                <hr>
            `;
            guestDetails.appendChild(guestDiv);
        });

        const checkInCheckboxes = document.querySelectorAll('.check-in-checkbox');
        checkInCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', event => {
                const name = event.target.getAttribute('data-name');
                const now = new Date();
                const checkInTime = now.toLocaleTimeString();
                const confirmMessage = `Are you sure you want to ${event.target.checked ? 'check-in' : 'check-out'} ${name} at ${checkInTime}?`;
                if (confirm(confirmMessage)) {
                    fetch('/check_in_guest', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ name })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.error) {
                            alert(data.error);
                            return;
                        }
                        lastAction = { type: 'check_in', name: name };
                        updateAttendeeList(data);
                        fetch('/get_checked_in_attendees')
                            .then(response => response.json())
                            .then(data => updateCheckedInList(data))
                            .catch(error => console.error('Error fetching checked-in attendees:', error));
                        updateGuestDetails([data.find(a => a.name === name)]); // Update only the specific guest
                        updateAttendanceStats(data);
                    })
                    .catch(error => console.error('Error checking in guest:', error));
                } else {
                    event.target.checked = !event.target.checked;
                }
            });
        });
    };

    const updateAttendanceStats = (data) => {
        const totalInvitees = data.length;
        const checkedInCount = data.filter(attendee => attendee.checked_in).length;
        const percentageCheckedIn = totalInvitees > 0 ? ((checkedInCount / totalInvitees) * 100).toFixed(2) : 0;
        attendanceStats.innerHTML = `Total Invitees: ${totalInvitees} | Checked-in: ${checkedInCount} (${percentageCheckedIn}%)`;
    };

    uploadForm.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(uploadForm);

        fetch('/upload_csv', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                uploadMessage.textContent = data.error;
                uploadMessage.style.color = 'red';
                return;
            }
            uploadMessage.textContent = data.message;
            uploadMessage.style.color = 'green';
            updateAttendeeList(data.attendees);
            fetch('/get_checked_in_attendees')
                .then(response => response.json())
                .then(data => updateCheckedInList(data))
                .catch(error => console.error('Error fetching checked-in attendees:', error));
            updateAttendanceStats(data.attendees);
            loadedFile.textContent = data.loaded_file;
        })
        .catch(error => console.error('Error uploading CSV:', error));
    });

    searchForm.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(searchForm);
        const name = formData.get('name');

        fetch('/search_guest', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            if (data.length === 0) {
                alert('No matching name found. Please verify the name and try again.');
            } else {
                updateGuestDetails(data);
            }
        })
        .catch(error => console.error('Error searching guest:', error));
    });

    menuSelect.addEventListener('change', event => {
        const option = event.target.value;
        if (option === 'reset') {
            fetch('/reset', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                    return;
                }
                updateAttendeeList(data.attendees);
                updateCheckedInList([]);
                updateAttendanceStats(data.attendees);
                loadedFile.textContent = 'No file loaded';
            })
            .catch(error => console.error('Error resetting data:', error));
        } else if (option === 'generateReport') {
            fetch('/generate_report')
                .then(response => response.blob())
                .then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'report.csv';
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                })
                .catch(error => console.error('Error generating report:', error));
        } else if (option === 'about') {
            alert('Event Attendance Management System\nVersion 1.0.2\nDeveloped by [Giancarlo Guimarães]\nContact: [giancarlo.guimaraes21@gmail.com]');
        }
    });

    undoButton.addEventListener('click', () => {
        if (lastAction) {
            fetch('/undo_check_in', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: lastAction.name })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                    return;
                }
                updateAttendeeList(data);
                fetch('/get_checked_in_attendees')
                    .then(response => response.json())
                    .then(data => updateCheckedInList(data))
                    .catch(error => console.error('Error fetching checked-in attendees:', error));
                updateGuestDetails([data.find(a => a.name === lastAction.name)]); // Update only the specific guest
                updateAttendanceStats(data);
                lastAction = null;
            })
            .catch(error => console.error('Error undoing check-in:', error));
        } else {
            alert('No action to undo.');
        }
    });

    saveButton.addEventListener('click', () => { // Ensure this block is present
        fetch('/save_attendees', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            alert(data.message);
        })
        .catch(error => console.error('Error saving attendees:', error));
    });

    // Initial fetch of attendees
    fetch('/get_attendees')
        .then(response => response.json())
        .then(data => {
            updateAttendeeList(data);
            fetch('/get_checked_in_attendees')
                .then(response => response.json())
                .then(data => updateCheckedInList(data))
                .catch(error => console.error('Error fetching checked-in attendees:', error));
            updateAttendanceStats(data);
        })
        .catch(error => console.error('Error fetching attendees:', error));

    // Update clock and countdown
    updateClock();
    setInterval(updateClock, 1000);
    updateCountdown();
});
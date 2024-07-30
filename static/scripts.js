document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('uploadForm');
    const addAttendeeForm = document.getElementById('addAttendeeForm');
    const removeAttendeeForm = document.getElementById('removeAttendeeForm');
    const checkInForm = document.getElementById('checkInForm');
    const undoCheckInForm = document.getElementById('undoCheckInForm');
    const attendeeList = document.getElementById('attendeeList');
    const menuSelect = document.getElementById('menuSelect');

    const updateAttendeeList = (data) => {
        attendeeList.innerHTML = '';
        data.forEach(attendee => {
            const attendeeDiv = document.createElement('div');
            attendeeDiv.className = attendee.checked_in ? 'checked-in' : '';
            attendeeDiv.innerHTML = `
                <p>Name: ${attendee.name}</p>
                <p>Email: ${attendee.email}</p>
                <p>Registration ID: ${attendee.registration_id}</p>
                <p>Checked In: ${attendee.checked_in ? 'Yes' : 'No'}</p>
                <hr>
            `;
            attendeeList.appendChild(attendeeDiv);
        });
    };

    const fetchAttendees = () => {
        fetch('/get_attendees')
            .then(response => response.json())
            .then(data => updateAttendeeList(data))
            .catch(error => console.error('Error fetching attendees:', error));
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
                alert(data.error);
                return;
            }
            updateAttendeeList(data);
        })
        .catch(error => console.error('Error uploading CSV:', error));
    });

    addAttendeeForm.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(addAttendeeForm);
        const attendee = {
            name: formData.get('name'),
            email: formData.get('email'),
            registration_id: formData.get('registration_id'),
            checked_in: false
        };

        fetch('/add_attendee', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(attendee)
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            updateAttendeeList(data.attendees);
        })
        .catch(error => console.error('Error adding attendee:', error));
    });

    removeAttendeeForm.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(removeAttendeeForm);
        const registration_id = formData.get('registration_id');

        fetch('/remove_attendee', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ registration_id })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            updateAttendeeList(data.attendees);
        })
        .catch(error => console.error('Error removing attendee:', error));
    });

    checkInForm.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(checkInForm);
        const registration_id = formData.get('registration_id');

        fetch('/check_in_attendee', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ registration_id })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            updateAttendeeList(data.attendees);
        })
        .catch(error => console.error('Error checking in attendee:', error));
    });

    undoCheckInForm.addEventListener('submit', event => {
        event.preventDefault();
        const formData = new FormData(undoCheckInForm);
        const registration_id = formData.get('registration_id');

        fetch('/undo_check_in', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ registration_id })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }
            updateAttendeeList(data.attendees);
        })
        .catch(error => console.error('Error undoing check-in:', error));
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
            })
            .catch(error => console.error('Error resetting data:', error));
        } else if (option === 'generateReport') {
            fetch('/generate_report')
                .then(response => response.blob())
                .then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'report.txt';
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                })
                .catch(error => console.error('Error generating report:', error));
        } else if (option === 'about') {
            alert('Event Attendance Management System\nVersion 1.0\nDeveloped by [Your Name]');
        }
    });

    // Initial fetch of attendees
    fetchAttendees();
});
// Main JavaScript file for Attendance System

// Auto-hide flash messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.style.display = 'none';
            }, 300);
        }, 5000);
    });
});

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    const inputs = form.querySelectorAll('input[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            input.style.borderColor = '#dc3545';
            isValid = false;
        } else {
            input.style.borderColor = '#e0e0e0';
        }
    });
    
    return isValid;
}

// Confirm delete actions
function confirmDelete(message) {
    return confirm(message || 'Are you sure you want to delete this item?');
}

// Format time remaining
function formatTimeRemaining(expiresAt) {
    const now = new Date();
    const expires = new Date(expiresAt);
    const diff = expires - now;
    
    if (diff <= 0) {
        return 'EXPIRED';
    }
    
    const minutes = Math.floor(diff / 60000);
    const seconds = Math.floor((diff % 60000) / 1000);
    
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

// Live attendance updates (for lecturer view)
function startLiveAttendanceUpdates(sessionId) {
    setInterval(() => {
        fetch(`/lecturer/attendance-live/${sessionId}`)
            .then(response => response.json())
            .then(data => {
                if (data.students) {
                    updateAttendanceList(data.students);
                    updateAttendanceStats(data.total_present, data.total_registered);
                }
                
                if (data.is_expired) {
                    document.querySelector('.badge-success')?.classList.replace('badge-success', 'badge-danger');
                    document.querySelector('.badge')?.textContent = 'Expired';
                }
            })
            .catch(error => console.error('Error updating attendance:', error));
    }, 3000); // Update every 3 seconds
}

function updateAttendanceList(students) {
    const tbody = document.getElementById('attendance-list');
    if (!tbody) return;
    
    tbody.innerHTML = students.map(student => `
        <tr>
            <td>${student.matric}</td>
            <td>${student.name}</td>
            <td>${student.time}</td>
        </tr>
    `).join('') || '<tr><td colspan="3" class="text-center">No attendance marked yet</td></tr>';
}

function updateAttendanceStats(present, total) {
    const presentElem = document.getElementById('total-present');
    const absentElem = document.getElementById('total-absent');
    const rateElem = document.getElementById('attendance-rate');
    
    if (presentElem) presentElem.textContent = present;
    if (absentElem) absentElem.textContent = total - present;
    if (rateElem) {
        const rate = total > 0 ? ((present / total) * 100).toFixed(1) : 0;
        rateElem.textContent = `${rate}%`;
    }
}

// Smooth scroll to top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Print QR code
function printQRCode() {
    window.print();
}

// Copy URL to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        alert('URL copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// Initialize tooltips (if using a library)
document.addEventListener('DOMContentLoaded', function() {
    // Add any initialization code here
    console.log('Attendance System loaded successfully');
});

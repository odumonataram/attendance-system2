import os

# Define all template contents
templates = {
    'templates/admin/lecturers.html': '''{% extends "base.html" %}

{% block title %}Lecturers - Admin{% endblock %}

{% block content %}
<div class="page-header">
    <h1>👨‍🏫 Lecturers</h1>
    <a href="{{ url_for('admin.add_lecturer') }}" class="btn btn-primary">➕ Add New Lecturer</a>
</div>

<div class="table-card">
    <table class="data-table">
        <thead>
            <tr>
                <th>Full Name</th>
                <th>Username</th>
                <th>Email</th>
                <th>Courses</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for lecturer in lecturers %}
            <tr>
                <td>{{ lecturer.full_name }}</td>
                <td>{{ lecturer.username }}</td>
                <td>{{ lecturer.email }}</td>
                <td>{{ lecturer.courses_taught|length }}</td>
                <td class="actions">
                    <a href="{{ url_for('admin.assign_courses', lecturer_id=lecturer.id) }}" class="btn btn-sm btn-secondary">Assign Courses</a>
                    <form method="POST" action="{{ url_for('admin.delete_user', user_id=lecturer.id) }}" style="display:inline;" onsubmit="return confirm('Are you sure you want to delete this lecturer?');">
                        <button type="submit" class="btn btn-sm btn-danger">Delete</button>
                    </form>
                </td>
            </tr>
            {% else %}
            <tr>
                <td colspan="5" class="text-center">No lecturers found</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}''',

    'templates/admin/add_lecturer.html': '''{% extends "base.html" %}

{% block title %}Add Lecturer - Admin{% endblock %}

{% block content %}
<div class="page-header">
    <h1>➕ Add New Lecturer</h1>
</div>

<div class="form-card">
    <form method="POST" action="{{ url_for('admin.add_lecturer') }}">
        <div class="form-group">
            <label for="username">Username *</label>
            <input type="text" id="username" name="username" class="form-control" required>
            <small>3-20 alphanumeric characters</small>
        </div>
        
        <div class="form-group">
            <label for="password">Password *</label>
            <input type="password" id="password" name="password" class="form-control" required>
            <small>Minimum 6 characters</small>
        </div>
        
        <div class="form-group">
            <label for="full_name">Full Name *</label>
            <input type="text" id="full_name" name="full_name" class="form-control" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email *</label>
            <input type="email" id="email" name="email" class="form-control" required>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn btn-primary">Add Lecturer</button>
            <a href="{{ url_for('admin.lecturers') }}" class="btn btn-secondary">Cancel</a>
        </div>
    </form>
</div>
{% endblock %}''',

    'templates/admin/assign_courses.html': '''{% extends "base.html" %}

{% block title %}Assign Courses - Admin{% endblock %}

{% block content %}
<div class="page-header">
    <h1>📚 Assign Courses to {{ lecturer.full_name }}</h1>
</div>

{% if existing_courses %}
<div class="info-card">
    <h3>Existing Courses</h3>
    <ul class="course-list">
        {% for course in existing_courses %}
        <li>{{ course.course_code }} - {{ course.course_name }} (Section {{ course.section }})</li>
        {% endfor %}
    </ul>
</div>
{% endif %}

<div class="form-card">
    <form method="POST" action="{{ url_for('admin.assign_courses', lecturer_id=lecturer.id) }}">
        <div id="courses-container">
            <div class="course-entry">
                <div class="form-row">
                    <div class="form-group">
                        <label>Course Code *</label>
                        <input type="text" name="course_code[]" class="form-control" placeholder="CSC301" required>
                        <small>Format: 3 letters + 3 digits</small>
                    </div>
                    
                    <div class="form-group">
                        <label>Course Name *</label>
                        <input type="text" name="course_name[]" class="form-control" placeholder="Data Structures" required>
                    </div>
                    
                    <div class="form-group">
                        <label>Section *</label>
                        <input type="text" name="section[]" class="form-control" placeholder="A" maxlength="5" required>
                    </div>
                </div>
            </div>
        </div>
        
        <button type="button" class="btn btn-secondary" onclick="addCourseField()">➕ Add Another Course</button>
        
        <div class="form-actions">
            <button type="submit" class="btn btn-primary">Assign Courses</button>
            <a href="{{ url_for('admin.lecturers') }}" class="btn btn-secondary">Cancel</a>
        </div>
    </form>
</div>

<script>
function addCourseField() {
    const container = document.getElementById('courses-container');
    const entry = document.createElement('div');
    entry.className = 'course-entry';
    entry.innerHTML = `
        <div class="form-row">
            <div class="form-group">
                <label>Course Code *</label>
                <input type="text" name="course_code[]" class="form-control" placeholder="CSC302" required>
            </div>
            <div class="form-group">
                <label>Course Name *</label>
                <input type="text" name="course_name[]" class="form-control" placeholder="Algorithms" required>
            </div>
            <div class="form-group">
                <label>Section *</label>
                <input type="text" name="section[]" class="form-control" placeholder="B" maxlength="5" required>
            </div>
        </div>
    `;
    container.appendChild(entry);
}
</script>
{% endblock %}''',
}

# Create all templates
for filepath, content in templates.items():
    full_path = f'/home/claude/attendance-system/{filepath}'
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f"Created: {filepath}")

print("All templates created successfully!")

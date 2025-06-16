from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Oracle Upgrade Advisor</title>
</head>
<body>
    <h2>Oracle Upgrade Advisor</h2>
    <form method="post">
        <label for="option">Choose an option:</label>
        <select name="option" id="option" required>
            <option value="">--Please select--</option>
            <option value="upgrade">Upgrade Implementation Plan</option>
            <option value="migration">Migration Plan</option>
        </select>
        <button type="submit">Submit</button>
    </form>
    {% if steps %}
    <h3>Implementation Steps:</h3>
    <ol>
      {% for step in steps %}
      <li>{{ step }}</li>
      {% endfor %}
    </ol>
    {% endif %}
</body>
</html>
'''

UPGRADE_STEPS = [
    "Analyze the current Oracle Database version and environment.",
    "Review Oracle's official documentation for the target upgrade version.",
    "Check hardware, OS, and software prerequisites.",
    "Take a full database backup.",
    "Install the new Oracle software (in a new Oracle home).",
    "Run pre-upgrade checks using Oracle's pre-upgrade tool.",
    "Resolve any issues found in the pre-upgrade checks.",
    "Perform a test upgrade on a non-production environment.",
    "Schedule downtime for production upgrade.",
    "Shut down applications and database.",
    "Perform the upgrade using Database Upgrade Assistant (DBUA) or command-line tools.",
    "Run post-upgrade scripts and checks.",
    "Test applications and validate data integrity.",
    "Monitor performance and address any post-upgrade issues."
]

MIGRATION_STEPS = [
    "Assess source and target environments (Oracle versions, OS, hardware).",
    "Choose the migration method (Data Pump, RMAN, GoldenGate, etc.).",
    "Plan for downtime and communicate with stakeholders.",
    "Take a full backup of the source database.",
    "Set up the target environment (install Oracle, configure OS, storage, etc.).",
    "If required, create tablespaces and users in the target database.",
    "Export data from the source database (using chosen tool).",
    "Transfer export files to the target environment.",
    "Import data into the target database.",
    "Run post-migration scripts (recompile objects, update stats, etc.).",
    "Perform data validation and application testing.",
    "Switch over production traffic to the new environment.",
    "Monitor system for issues post-migration."
]

@app.route('/', methods=['GET', 'POST'])
def advisor():
    steps = None
    if request.method == 'POST':
        option = request.form.get('option')
        if option == 'upgrade':
            steps = UPGRADE_STEPS
        elif option == 'migration':
            steps = MIGRATION_STEPS
    return render_template_string(HTML_FORM, steps=steps)

if __name__ == '__main__':
    app.run(debug=True)

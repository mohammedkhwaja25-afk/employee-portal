from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Employee Portal</h1>
    <h2>Welcome Mohammed!</h2>

    <hr>

    <h3>Available Pages</h3>

    <ul>
        <li><a href="/employees">Employees</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/health">Health</a></li>
    </ul>
    """

@app.route("/employees")
def employees():
    return """
    <h2>Employee List</h2>

    <table border="1" cellpadding="10">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
        </tr>

        <tr>
            <td>101</td>
            <td>John</td>
            <td>IT</td>
        </tr>

        <tr>
            <td>102</td>
            <td>Sarah</td>
            <td>HR</td>
        </tr>

        <tr>
            <td>103</td>
            <td>David</td>
            <td>Finance</td>
        </tr>
    </table>

    <br>

    <a href="/">Home</a>
    """

@app.route("/about")
def about():
    return """
    <h2>Employee Portal</h2>

    <p>Version : 1.0</p>

    <p>Powered by Flask</p>

    <a href="/">Home</a>
    """

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "Employee Portal",
        "version": "1.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

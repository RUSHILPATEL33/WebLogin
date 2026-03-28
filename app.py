from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)   # ✅ MUST BE AT TOP

# Home → redirect to login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Optional: remove favicon error
@app.route('/favicon.ico')
def favicon():
    return '', 204

# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save user
        with open('users.txt', 'a') as f:
            f.write(f"{username},{password}\n")

        return render_template('register.html', message="✅ Registered Successfully!")

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with open('users.txt', 'r') as f:
                users = f.readlines()
        except FileNotFoundError:
            users = []

        for user in users:
            stored_user, stored_pass = user.strip().split(',')

            if username == stored_user and password == stored_pass:
                return render_template('login.html', message=f"🎉 Welcome {username}!")

        return render_template('login.html', message="❌ Invalid Credentials")

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
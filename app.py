from flask import Flask, render_template
import controllers

app = Flask(__name__, template_folder='views')

app.register_blueprint(controllers.main)

# comment this out using a WSGI like gunicorn
# if you dont, gunicorn will ignore it anyway
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)

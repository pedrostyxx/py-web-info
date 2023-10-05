from flask import Flask, request, jsonify, render_template_string
from user_agents import parse

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)

    client_ip = request.remote_addr
    device = user_agent.device.family
    browser = user_agent.browser.family
    browser_version = user_agent.browser.version_string
    browser_language = request.headers.get('Accept-Language')

    response_data = {
        'user_agent': user_agent_string,
        'client_ip': client_ip,
        'device': device,
        'browser': browser,
        'browser_version': browser_version,
        'browser_language': browser_language,
    }

    return jsonify(response_data)

@app.route('/')
def index():
    return render_template_string('index.html')


if __name__ == '__main__':
    app.run(debug=True)

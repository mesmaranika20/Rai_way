# from core.request import parse_json_body
# from core.responses import send_json, send_404
# from services.auth_service import get_all_users
# from core.responses import send_json 


# def register_user(handler):
#     data = parse_json_body(handler)
#     return send_json(handler, 201, register(data["username"], data["password"]))

# def login_user(handler):
#     data = parse_json_body(handler)
#     user = login(data["username"], data["password"])
#     return send_json(handler, 200, user) if user else send_404(handler)

# from core.request import parse_json_body
# from core.responses import send_json
# from services.payroll_service import service_get_all, service_create

# def get_all_payroll(handler):
#     return send_json(handler, 200, service_get_all())

# def create_payroll(handler):
#     data = parse_json_body(handler)
#     service_create(data)
#     return send_json(handler, 201, {"created": True})

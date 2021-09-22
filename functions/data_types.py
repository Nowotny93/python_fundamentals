def get_result(data_type, data):
    if data_type == "int":
        result = int(data) * 2
        return result
    elif data_type == "real":
        result = float(data) * 1.5
        return f"{result:.2f}"
    elif data_type == "string":
        result = "$" + data + "$"
        return result

data_type = input()
data = input()
print(get_result(data_type, data))
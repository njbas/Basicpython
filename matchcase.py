response_code = 200

match response_code:
    case 200:
        print("OK")
    case 404:
        print("Not found")
    case 500:
        print("Internal Sever Error")

def format_data_for_display(people: list[dict]):
    res_list = []
    for di in people:
        res_string = di.get("given_name") + " "
        res_string += di.get("family_name")
        res_string += ": " + di.get("title")
        res_list.append(res_string)
    
    return res_list


def format_data_for_excel(people: list[dict]):
    res_string = "given,family,title\n"
    for di in people:
        res_string += di.get("given_name") + ","
        res_string += di.get("family_name") + ","
        res_string += di.get("title") + "\n"
    
    return res_string

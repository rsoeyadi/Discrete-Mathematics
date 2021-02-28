def format_prop(prop):
    # BASE CASE: #####################################
    if len(prop) < 2:
        return prop[0]
    ##################################################

    # UNARY OPERATOR (not): ##########################
    if 2 == len(prop):
        # the following two variable declarations are missing LHS #
        op = prop[0]  # missing LHS
        prop = prop[1]  # missing LHS

        if "not" == op:
            formatted_prop = '(' + op + ' ' + format_prop(prop) + ')'
            return formatted_prop
        else:
            raise ValueError("Unary proposition is not not.")
    ##################################################

    # BINARY OPERATOR (and, or, if, iff, xor): #######
    elif 3 == len(prop):
        # the following three variable declarations are missing LHS #
        op = prop[0]  # missing LHS
        prop1 = prop[1]  # missing LHS
        prop2 = prop[2]  # missing LHS

        if op not in ("if", "iff", "or", "and", "xor"):
            raise ValueError("Binary proposition does not have valid connectives.")

        # change "if" and "iff" representation
        if "if" == op:
            op = "->"
        elif "iff" == op:
            op = "<->"

        # format left and right sides of a binary operation
        left_prop = format_prop(prop[1])
        right_prop = format_prop(prop[2])

        if len(left_prop.split()) == 1 and len(right_prop.split()) > 1:
            formatted_prop = "(" + left_prop + " " + op + " " + right_prop + ")"
        elif len(left_prop.split()) > 1 and len(right_prop.split()) == 1:
            formatted_prop = "(" + left_prop + " " + op + " " + right_prop + ")"
        elif len(left_prop.split()) == 1 and len(right_prop.split()) == 1:
            formatted_prop = left_prop + " " + op + " " + right_prop
        else:
            formatted_prop = "(" + left_prop + ") " + op + " " + "(" + right_prop
        return formatted_prop
    ####################################################

    # INVALID LENGTH ####################################
    else:
        raise ValueError("Proposition incorrect length.")
    #####################################################


def main():
    lst2 = ["not", ["p1"]]
    lst3 = ["and", ["p1"], ["p2"]]
    lst4 = ["iff", ["p1"], ["p2"]]
    lst5 = ["if", ["and", ["p1"], ["not", ["p2"]]], ["p3"]]
    lst6 = ["iff", ["p1"], ["or", ["p2"], ["not", ["p3"]]]]

    print(format_prop(lst2))
    print(format_prop(lst3))
    print(format_prop(lst4))
    print(format_prop(lst5))
    print(format_prop(lst6))


main()
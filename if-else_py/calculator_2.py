import math

PI = math.pi
E = math.e
TAU = math.tau

# --- Simple Calculator ---
add = lambda x, y: x + y
subtract = lambda x, y: x - y
divide = lambda x, y: x / y
multiply = lambda x, y: x * y

ratio = lambda theta: theta / 360

# --- Circle ---
circle_radius_d = lambda d: d / 2
circle_radius_a_pi = lambda a: math.sqrt(a / PI)
circle_radius_c_pi = lambda c: c / (2 * PI)
circle_diameter_r = lambda r: 2 * r
circle_diameter_a_pi = lambda a: 2 * math.sqrt(a / PI)
circle_diameter_c_pi = lambda c: c / PI
circle_circumference_r_pi = lambda r: 2 * PI * r
circle_circumference_r = lambda r: f"{2 * r}π"
circle_circumference_d_pi = lambda d: PI * d
circle_circumference_d = lambda d: f"{d}π"
circle_circumference_a_pi = lambda a: 2 * PI * circle_radius_a_pi(a)
circle_circumference_a = lambda a: f"{2 * circle_radius_a_pi(a)}π"
circle_area_r_pi = lambda r: PI * (r ** 2)
circle_area_r = lambda r: f"{r ** 2}π"
circle_area_d_pi = lambda d: PI * (circle_radius_d(d) ** 2)
circle_area_d = lambda d: f"{circle_radius_d(d) ** 2}π"
circle_area_c_pi = lambda c: PI * (circle_radius_c_pi(c) ** 2)
circle_area_c = lambda c: f"{circle_radius_c_pi(c) ** 2}π"
circle_arc_length_r_pi = lambda r, theta: circle_circumference_r_pi(r) * (ratio(theta))
circle_arc_length_r = lambda r, theta: f"{(2 * r * (ratio(theta)))}π"
circle_arc_length_d_pi = lambda d, theta: circle_circumference_r_pi(circle_radius_d(d)) * (ratio(theta))
circle_arc_length_d = lambda d, theta: f"{2 * r * (ratio(theta))}π"
circle_arc_length_a_pi = lambda a, theta: circle_circumference_r_pi(circle_radius_a_pi(a)) * (ratio(theta))
circle_arc_length_a = lambda a, theta: f"{2 * (a / PI) * (ratio(theta))}π"
circle_arc_length_c = lambda c, theta: c * (ratio(theta))
circle_sector_area_r_pi = lambda r, theta: circle_area_r_pi(r) * (ratio(theta))
circle_sector_area_r = lambda r, theta: f"{circle_area_r(r) * (ratio(theta))}π"
circle_sector_area_d_pi = lambda d, theta: circle_area_d_pi(d) * (ratio(theta))
circle_sector_area_d = lambda d, theta: f"{(circle_diameter_r(d) ** 2) * (ratio(theta))}π"
circle_sector_area_c_pi = lambda c, theta: circle_area_r_pi(circle_radius_c_pi(c)) * (ratio(theta))
circle_sector_area_c = lambda c, theta: f"{(circle_radius_c_pi(c) ** 2) * (ratio(theta))}π"
circle_sector_area_a_pi = lambda a, theta: circle_area_r_pi(circle_radius_a_pi(a)) * (ratio(theta))
circle_arc_chord_r = lambda r, theta: circle_diameter_r(r) * math.sin(math.radians(theta) / 2)
circle_arc_chord_d = lambda d, theta: d * math.sin(math.radians(theta) / 2)



def main():
    input_list = []
    while True:
        try:
            opening = int(input("""
    THE ULTIMATE PYCULATOR
    1) Get Started
    2) Start Calculating
            """))
        except ValueError:
            pass
        else:
            if opening == 1:
                print(""" 

                """)
            elif opening == 2:
                while True:
                    try:
                        user = input()
                        user = check_float_int(user)
                        for c in user:
                            if c:
                                input_list.append(c)
                        if user is str:
                            user = user.lower().strip()
                            if 'circle' == user:
                                property = input().lower().strip()
                                match property:
                                    case 'help' | '--help':
                                        print(circleh)
                                    case 'r':
                                        user_input_as_list = []
                                        try:
                                            get_user = input()
                                            for index, character in enumerate(get_user):
                                                if character:
                                                    try:
                                                        character = float(character)
                                                    except ValueError:
                                                        character = character.lower
                                                    user_input_as_list.append(character)

                                        except (IndexError, ValueError):

                                    case 'd':
                            elif '=' in input_list:
                                index_start = 0
                                for i, c in enumerate(input_list):
                                    if c == "=":
                                        num1 = int(''.join(input_list[index_start:i]))
                                        index = i
                                        num1 = int(num1)
                                    elif c == "+":
                                        num1 = int(''.join(input_list[index_start:i]))
                                    elif c == '-':
                                        int(num1)
                                    

def check_float_int(string) -> str:
    """
    Takes 1 arguments, 1 string.
    String type MUST be a str.
    """
    try:
        fi = float(string)
    except ValueError:
        try:
            fi = int(string)
        except ValueError:
            return string
        else:
            return fi
    else:
        return fi

def simply_calculate(number_1: int | float, number_2: int | float, operator: str | None = None):
    """
    Takes 3 arguments, 2 number and 1 for operator.
    Operator MUST be the followings:
        '+' | '-' | '/' | '*'
    If operator None, all operation will be run. 
    """
    try:
        if operator is None:
            return add(number_1, number_2), subtract(number_1, number_2), divide(number_1, number_2), multiply(number_1, number_2)
        elif operator is not None:
            match operator:
                case '+':
                    return add(number_1, number_2)
                case '-':
                    return subtract(number_1, number_2)
                case '/':
                    return divide(number_1, number_2)
                case '*':
                    return multiply(number_1, number_2)
        else:
            raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError

if __name__ == "__main__":
    main()
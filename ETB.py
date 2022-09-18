
#________________________________________________________________________________________________________________________________

class etb_handle():
    user_vars = {}

    def __init__(self, eng_cmd: str) -> None:
        self.eng_cmd = str(eng_cmd).lower()

    def decode_cmd(self) -> bool:
        num_of_params = self.eng_cmd.count(' ')
        str_cmd = self.eng_cmd.strip().split(' ', num_of_params)

        match str_cmd[0]:
            case 'set':
                var_to_set = str_cmd[1]
                value_to_set = str_cmd[3]

                if value_to_set.isnumeric(): #num
                    if value_to_set.isdigit():
                        value_to_set = int(value_to_set)
                    else: 
                        value_to_set = float(value_to_set)

                elif value_to_set == 'true': #bool
                    value_to_set = True
                elif value_to_set == 'false': #bool
                    value_to_set = False
                elif value_to_set == 'none': #bool
                    value_to_set = None

                else: #str
                    value_to_set = self.text_handler(value_to_set)

                self.user_vars[var_to_set] = value_to_set

                return True
            case 'display':
                text = ' '.join(str_cmd[1:])
                print(self.text_handler(text))

                return True
            case _:
                return False

    def text_handler(self, text: str) -> str:
        text = text.replace(
            r' newline ', '\n').replace(
                r' tab ', '\t').replace(
                    r' reset caret ', '\r').replace(
                        r'\\', '\\')
        for var in self.user_vars.keys():
            text = text.replace(f'variable {var}', f'{self.user_vars[f"{var}"]}')

        return text


#________________________________________________________________________________________________________________________________

def input_cycle() -> None:
    while True: 
        try: 
            eng_cmd = input('> ')

            p = etb_handle(eng_cmd)
            ret = p.decode_cmd()
            if not ret:
                print('\tcommand not found, please check spelling & grammar')
        except KeyboardInterrupt:
            break

def main() -> None:
    print('Hello World!\n')
    input_cycle()

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': 
    input_cycle()
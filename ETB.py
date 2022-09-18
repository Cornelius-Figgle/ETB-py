
#________________________________________________________________________________________________________________________________

class etb_handle():
    vars = {}

    def __init__(self, eng_cmd: str) -> None:
        self.eng_cmd = str(eng_cmd).lower()

    def decode_cmd(self) -> bool:
        num_of_params = self.eng_cmd.count(' ')
        str_cmd = self.eng_cmd.strip().split(' ', num_of_params)

        match str_cmd[0]:
            case 'set': # `set x to 4`
                var_to_set = str_cmd[1]
                value_to_set = str_cmd[3]

                self.vars[var_to_set] = value_to_set

                return True
            case 'display': # `display x`
                try: print(self.vars[''.join(str_cmd[1:])])
                except KeyError: print(' '.join(str_cmd[1:]))

                return True
            case _:
                return False

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

#________________________________________________________________________________________________________________________________

class etb_handle():

    def __init__(self, eng_cmd: str) -> None:
        self.eng_cmd = str(eng_cmd).lower()

        self.vars = {}

    def decode_cmd(self) -> bool:
        num_of_params = self.eng_cmd.count(' ')
        str_cmd = self.eng_cmd.strip().split(' ', num_of_params)

        match str_cmd[0]:
            case 'set':
                var_to_set = str_cmd[1]
                value_to_set = str_cmd[3]

                self.vars[var_to_set] = value_to_set

                return self.vars[var_to_set]
            case 'display':
                return ' '.join(str_cmd[1:])
            case _:
                return None

#________________________________________________________________________________________________________________________________

def input_cycle() -> None:
    while True: 
        try: 
            eng_cmd = input('> ')

            p = etb_handle(eng_cmd)
            ret = p.decode_cmd()
            print(ret)
        except KeyboardInterrupt:
            break

def main() -> None:
    print('Hello World!\n')
    input_cycle()

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': 
    input_cycle()
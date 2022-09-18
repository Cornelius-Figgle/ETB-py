
#________________________________________________________________________________________________________________________________

class etb_handle():

    def __init__(self, eng_cmd: str) -> None:
        self.eng_cmd = str(eng_cmd).lower()

        self.all_starters = [
            'set',
            'display',
            'if'
        ]

        self.cmd_to_use = None

    def decode_start(self) -> int | None:
        starter = self.eng_cmd.split(' ', 0)

        if starter in self.all_starters:
            self.cmd_to_use = self.all_starters.index(starter)
            return self.cmd_to_use
        else:
            return None

    def determine_rest(self):
        pass

#________________________________________________________________________________________________________________________________

def input_cycle() -> None:
    while True: 
        try: 
            eng_cmd = input('> ')

            p = etb_handle(eng_cmd)
            p.decode_start()
            p.determine_rest()
        except KeyboardInterrupt:
            break

def main() -> None:
    print('Hello World!\n')
    input_cycle()

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': 
    input_cycle()
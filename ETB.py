

#________________________________________________________________________________________________________________________________

class etb_handle():
    def __init__(self, eng_cmd: str) -> None:
        self.eng_cmd = str(eng_cmd)

    def decode_start(self) -> str:
        return self.eng_cmd.split(' ', 0)

#________________________________________________________________________________________________________________________________

def input_cycle() -> None:
    eng_cmd = input('> ')

    p = etb_handle(eng_cmd)
    p.decode_start()

def main() -> None:
    print('Hello World!\n')

    while True: 
        try: 
            input_cycle()
        except KeyboardInterrupt:
            break

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': 
    main()
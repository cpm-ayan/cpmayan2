import random
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from ayan import Ayan

__CHANNEL_USERNAME__ = "Ayan"
__GROUP_USERNAME__   = "Aayan"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold green] ♕  Creator[/bold green]: Ayan.")
    console.print(f"[bold green]♕  Facebook[/bold green]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue] or [bold blue]@{__GROUP_USERNAME__}[/bold blue].")
    console.print("==================================================")
    console.print("[bold yellow]! Note[/bold yellow]: Энэ хэрэгслийг ашиглахаасаа өмнө CPM аккоунтаасаа гарна уу !.", end="\n\n")

def get_player_data(cpm):
    data = cpm.get_player_data().get('data')
    console.print("[bold][red]========[/red][ PLAYER DETAILS ][red]========[/red][/bold]")
    console.print(f"[bold green] Нэр   [/bold green]: {data.get('Name') if 'Name' in data else 'UNDEFINED'}.")
    console.print(f"[bold green] ID    [/bold green]: {data.get('localID') if 'localID' in data else 'UNDEFINED'}.")
    console.print(f"[bold green] Мөнгө [/bold green]: {data.get('money') if 'money' in data else 'UNDEFINED'}.")
    console.print(f"[bold green] Зоос  [/bold green]: {data.get('coin') if 'coin' in data else 'UNDEFINED'}.")

def get_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold][red]========[/red][ ACCESS KEY DETAILS ][red]========[/red][/bold]")
    console.print(f"[bold green] Зөвшөөрлийн түлхүүр[/bold green]: {data.get('access_key') }.")
    console.print(f"[bold green] Телеграм ID        [/bold green]: {data.get('telegram_id')}.")
    console.print(f"[bold green] Үлдэгдэл           [/bold green]: {data.get('coins') if not data.get('is_unlimited') else 'Unlimited'}.")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold]➤ Емайл[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold]➤ Нууц үг[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold]➤ Зөвшөөрлийн түлхүүр[/bold]", "Access Key", password=False)
        console.print("[bold cyan]↻ Нэвтэрхийг оролдож байна[/bold cyan]: ", end=None)
        cpm = Ayan(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]Аккоунт олдсонгүй![/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]Нууц үг буруу байна![/bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red] Зөвшөөрлийн түлхүүр буруу байна![/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]Дахин оролдоно уу[/bold red].")
                console.print("[bold yellow]! Note:[/bold yellow]: Талбаруудыг бүрэн бөглөсөн эсэхээ шалгаарай !.")
                sleep(2)
                continue
        else:
            console.print("[bold green]АМЖИЛТТАЙ![/bold green].")
            sleep(2)
        while True:
            banner(console)
            get_player_data(cpm)
            get_key_data(cpm)
            console.print("[bold cyan](01): Мөнгө нэмэгдүүлэх ~ 9999999K[/bold cyan]")
            console.print("[bold cyan](02): Зоосыг нэмэгдүүлэх ~ 99999999K[/bold cyan]")
            console.print("[bold cyan](03): Хаан зэрэглэл ~ 99999999K[/bold cyan]")
            console.print("[bold cyan](04): ID-г өөрчлөх ~ 999999999K[/bold cyan]")
            console.print("[bold cyan](05): Нэрийг өөрчлөх ~ 999999K[/bold cyan]")
            console.print("[bold cyan](06): Нэрийг өөрчлөх (Солонгон) ~ 99999999K[/bold cyan]")
            console.print("[bold cyan](07): Бүх машины түгжээг тайлах ~ 99999999K[/bold cyan]")
            console.print("[bold cyan](08): Бүртгэл устгах ~ 9999999999K[/bold cyan]")
            console.print("[bold cyan](09): Бүртгэл үүсгэх ~ 99999999999K[/bold cyan]")
            console.print("[bold cyan](10): Найзуудыг устгах ~ 9999999999K[/bold cyan]")
            console.print("[bold cyan](11): Дугаарын хавтан ~ 9999999OOOOOK[/bold cyan]")
            console.print("[bold cyan](00): Гарах[/bold cyan]", end="\n\n")
            service = IntPrompt.ask("[bold]➤ Үйлчилгээ сонгоно уу [red][0-9 ээс 0][/red][/bold]", choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"], show_choices=False)
            if service == 0: # Exit
                console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
            elif service == 1: # Increase Money
                console.print("[bold cyan]✶ Та хэр их мөнгө хүсч байгаагаа оруулна уу.[/bold cyan]")
                amount = IntPrompt.ask("[bold]➤ Дүн[/bold]")
                console.print("[bold cyan]↺ Таны өгөгдлийг хадгалж байна[/bold cyan]: ", end=None)
                if cpm.set_player_money(amount):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Та гарахыг хүсэж байна уу ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                    console.print("[bold yellow]✶ Дахин оролдоно уу.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                console.print("[bold cyan]✶ Та хэр их зоос хүсч байгаагаа оруулна уу.[/bold cyan]")
                amount = IntPrompt.ask("[bold]➤ Дүн[/bold]")
                console.print("[bold cyan]↺ Таны өгөгдлийг хадгалж байна[/bold cyan]: ", end=None)
                if cpm.set_player_coins(amount):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Та гарахыг хүсэж байна уу ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                    console.print("[bold yellow]✶ Дахин оролдоно уу.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold cyan]↺ Танд хааны зэрэглэлийг өгч байна[/bold cyan]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                    console.print("=====================")                  
                    if answ == "y": console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэйl[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                    console.print("[bold yellow]✶ Дахин оролдоно уу.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold cyan]✶ Шинэ ID-гаа оруулна уу.[/bold cyan]")
                new_id = Prompt.ask("[bold]➤ ID[/bold]")
                console.print("[bold cyan]↺ Таны өгөгдлийг хадгалж байна[/bold cyan]: ", end=None)
                if cpm.set_player_localid(new_id):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Та гарахыг хүсэж байна уу ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                    console.print("[bold yellow]✶ Дахин оролдоно уу.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold cyan]✶ Шинэ нэрээ оруулна уу.[/bold cyan]")
                new_name = Prompt.ask("[bold]➤ Нэр[/bold]")
                console.print("[bold cyan]↺ Таны өгөгдлийг хадгалж байна[/bold cyan]: ", end=None)
                if cpm.set_player_name(new_name):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Та гарахыг хүсэж байна уу ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                    console.print("[bold yellow]✶ Дахин оролдоно уу.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print("[bold cyan]✶ Шинэ солонгон нэрээ оруулна уу.[/bold cyan]")
                new_name = Prompt.ask("[bold]➤ Нэр[/bold]")
                console.print("[bold cyan]↺ Таны өгөгдлийг хадгалж байна[/bold cyan]: ", end=None)
                if cpm.set_player_name(rainbow_gradient_string(new_name)):
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Та гарахыг хүсэж байна уу ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                    console.print("[bold yellow]✶ Дахин оролдоно уу.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Unlock Cars
                console.print("[bold cyan]↺ Бүх машины түгжээг тайлж байна![/bold cyan]: ", end=None)
                if cpm.unlock_all_cars():
                    console.print("[bold green]АМЖИЛТТАЙ.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Та гарахыг хүсэж байна уу ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]АМЖИЛТГҮЙ.[/bold red]")
                    console.print("[bold yellow]✶ Дахин оролдоно уу.[/bold yellow]")
                    sleep(2)
                    continue      
            elif service == 8: # Account Delete
                console.print("[bold cyan]✶ Бүртгэлээ устгасны дараа буцах арга байхгүй !!.[/bold cyan]")
                answ = Prompt.ask("[bold cyan]➤ Та энэ бүртгэлийг нээрэнгээсээ устгахыг хүсэж байна уу ?![/bold cyan]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold cyan]↺ Таны бүртгэлийг устгаж байна[/bold cyan]: [bold green]SUCCESSFUL.[/bold green].")
                    console.print("==================================")
                    console.print(f"[bold yellow]✴ Манай хэрэгслийг ашигласанд баярлалаа, манай телеграм сувагт нэгдээрэй[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                else: continue
            elif service == 9: # Account Register
                console.print("[bold cyan]✶ Registring new Account.[/bold cyan]")
                acc2_email = prompt_valid_value("[bold]➤ Account Email[/bold]", "Email", password=False)
                acc2_password = prompt_valid_value("[bold]➤ Account Password[/bold]", "Password", password=False)
                console.print("[bold cyan]↺ Creating new Account[/bold cyan]: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    console.print(f"[bold yellow]! You've been automatically signed in as[/bold yellow]: [blue]{acc2_email}[/blue]")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ This email is already exists !.[/bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[bold cyan]↺ Deleting your Friends[/bold cyan]: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 11: # Number Plates
                console.print("[bold cyan]↺ Giving you a Number Plates[/bold cyan]: ", end=None)
                if cpm.set_player_plates():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan]➤ Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow]✴ Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow]✶ Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            else:   continue
            break
        break
    

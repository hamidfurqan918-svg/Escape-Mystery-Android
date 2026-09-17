# ESCAPE MYSTERY — ANDROID / TABLET
# Touch-friendly Kivy port using the EXACT 50 LEVELS from the supplied Pygame source.
import json, os, time
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

LEVELS = [{'kind': 'choice', 'clue': 'A clock shows 3:15. What is the smaller angle?', 'options': ['0°', '7.5°', '15°', '30°'], 'answer': '7.5°', 'item': 'BRASS KEY', 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Find the next number: 2, 6, 12, 20, 30, ?', 'options': ['40', '41', '42', '44'], 'answer': '42', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'If every door in this room is locked and this is a door, what is true?', 'options': ['It is locked', 'It is open', 'It is broken', 'Unknown'], 'answer': 'It is locked', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Which word does NOT belong?', 'options': ['Triangle', 'Square', 'Circle', 'Cube'], 'answer': 'Cube', 'item': 'COIN', 'need': None, 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: enter the next value in 2, 4, 8, 16, ?', 'options': [], 'answer': '32', 'item': 'BLUE CARD', 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Which number is divisible by both 3 and 5?', 'options': ['14', '20', '30', '44'], 'answer': '30', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Exactly three switches must be ON. Their numbers must add to 9.', 'options': ['1 + 3 + 5', '1 + 2 + 5', '2 + 3 + 4', '1 + 4 + 5'], 'answer': '1 + 3 + 5', 'item': None, 'need': None, 'room': None}, {'kind': 'sequence_lock', 'clue': 'SEQUENCE LOCK: A, C, F, J, O, ?', 'options': [], 'answer': 'U', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Order: smallest first, heaviest second, readable last.', 'options': ['Coin - Table - Book', 'Book - Coin - Table', 'Table - Book - Coin', 'Coin - Book - Table'], 'answer': 'Coin - Table - Book', 'item': 'NOTE', 'need': None, 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: calculate 18% of 200.', 'options': [], 'answer': '36', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Find the missing number: 5, 10, 20, 40, ?', 'options': ['60', '70', '80', '90'], 'answer': '80', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'This door requires the BRASS KEY from an earlier room. A=1, B=2, C=3. What is CAB?', 'options': ['5', '6', '7', '8'], 'answer': '6', 'item': None, 'need': 'BRASS KEY', 'room': None}, {'kind': 'choice', 'clue': 'Which number is prime?', 'options': ['21', '29', '33', '39'], 'answer': '29', 'item': None, 'need': None, 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: 3, 6, 12, 24, ?', 'options': [], 'answer': '48', 'item': None, 'need': None, 'room': None}, {'kind': 'sequence_lock', 'clue': 'SEQUENCE LOCK: Z, X, V, T, ?', 'options': [], 'answer': 'R', 'item': 'GOLD KEY', 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'A box has 7 red balls and 5 blue balls. Total?', 'options': ['10', '11', '12', '13'], 'answer': '12', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Three locks show 4, 6, 9. Divide them by 4, 3, 4.', 'options': ['1-2-2', '2-2-3', '1-3-2', '4-2-1'], 'answer': '1-2-2', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'What is the only even prime number?', 'options': ['0', '1', '2', '4'], 'answer': '2', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Greater than 40, less than 50, divisible by 3.', 'options': ['41', '42', '45', '49'], 'answer': '42', 'item': None, 'need': None, 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: 1, 4, 9, 16, 25, ?', 'options': [], 'answer': '36', 'item': 'SILVER KEY', 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Shift each letter 8 places forward: C A T.', 'options': ['KIB', 'JHB', 'KIC', 'LJB'], 'answer': 'KIB', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Which shape has exactly 5 sides?', 'options': ['Triangle', 'Square', 'Pentagon', 'Hexagon'], 'answer': 'Pentagon', 'item': None, 'need': 'BLUE CARD', 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: 3 keys cost 15 coins. Cost of 7 keys?', 'options': [], 'answer': '35', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Which number is NOT a multiple of 4?', 'options': ['12', '20', '28', '30'], 'answer': '30', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Which is a perfect square AND odd?', 'options': ['45', '48', '49', '54'], 'answer': '49', 'item': 'RED CARD', 'need': None, 'room': None}, {'kind': 'choice', 'clue': '60 km in 1 hour. How far in 3 hours?', 'options': ['120 km', '150 km', '180 km', '240 km'], 'answer': '180 km', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'A + B = 10 and A = 6. What is B?', 'options': ['2', '3', '4', '5'], 'answer': '4', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'What is 7 × 8?', 'options': ['54', '56', '58', '64'], 'answer': '56', 'item': None, 'need': None, 'room': None}, {'kind': 'input', 'clue': 'CODE LOCK: first digit is 2 and second digit is 5. Enter the first two digits.', 'options': [], 'answer': '25', 'item': None, 'need': None, 'room': None}, {'kind': 'sequence_lock', 'clue': 'SEQUENCE LOCK: B, D, G, K, P, ?', 'options': [], 'answer': 'V', 'item': 'GREEN CARD', 'need': None, 'room': None}, {'kind': 'choice', 'clue': '10 apples shared equally among 2 people. Each gets?', 'options': ['2', '4', '5', '8'], 'answer': '5', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'This room requires the BLUE CARD. What is 100 - 37?', 'options': ['53', '63', '73', '83'], 'answer': '63', 'item': None, 'need': 'BLUE CARD', 'room': None}, {'kind': 'color_lock', 'clue': 'COLOR LOCK: the panel flashes RED, BLUE, RED, GREEN. Which color is third?', 'options': [], 'answer': 'RED', 'item': None, 'need': None, 'room': None}, {'kind': 'sequence_lock', 'clue': 'MEMORY/SEQUENCE LOCK: 1, 1, 2, 3, 5, 8, ?', 'options': [], 'answer': '13', 'item': None, 'need': None, 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: what is 9 × 9?', 'options': [], 'answer': '81', 'item': 'VAULT KEY', 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Father is 40 and son is 10. In how many years is father twice son?', 'options': ['10', '15', '20', '25'], 'answer': '20', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Which number is divisible by 9?', 'options': ['36', '42', '52', '58'], 'answer': '36', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Start at (1,1). Right 5, down 1. Finish?', 'options': ['(5,1)', '(6,1)', '(6,2)', '(7,2)'], 'answer': '(6,2)', 'item': None, 'need': None, 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: 144 ÷ 12 = ?', 'options': [], 'answer': '12', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Three doors: Door 1 unsafe, Door 2 unsafe. Which remains?', 'options': ['Door 1', 'Door 2', 'Door 3', 'All doors'], 'answer': 'Door 3', 'item': 'MASTER CARD', 'need': None, 'room': None}, {'kind': 'choice', 'clue': '15 + 27 = ?', 'options': ['40', '41', '42', '43'], 'answer': '42', 'item': None, 'need': None, 'room': None}, {'kind': 'input', 'clue': 'CODE LOCK: increase every digit of 1234 by 1. Enter result.', 'options': [], 'answer': '2345', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Which is both a multiple of 5 and even?', 'options': ['15', '20', '25', '35'], 'answer': '20', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Monday + 10 days = ?', 'options': ['Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'answer': 'Thursday', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Rehan before Ali, Ali before Zoya, Zoya before Hamza. Who is third?', 'options': ['Rehan', 'Ali', 'Zoya', 'Hamza'], 'answer': 'Zoya', 'item': None, 'need': 'SILVER KEY', 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: 24 keys. One quarter are golden. How many?', 'options': [], 'answer': '6', 'item': None, 'need': None, 'room': None}, {'kind': 'choice', 'clue': 'Repeating sound when you walk in an empty room?', 'options': ['Footsteps', 'Water', 'Bell', 'Wind'], 'answer': 'Footsteps', 'item': None, 'need': None, 'room': None}, {'kind': 'number_lock', 'clue': 'NUMBER LOCK: 11 × 11 = ?', 'options': [], 'answer': '121', 'item': None, 'need': None, 'room': None}, {'kind': 'sequence_lock', 'clue': 'SEQUENCE LOCK: smallest to largest: 0.2, 0.02, 0.22', 'options': [], 'answer': '0.02-0.2-0.22', 'item': None, 'need': None, 'room': None}, {'kind': 'input', 'clue': 'MASTER CODE: calculate 5×2, 2+4, 10÷2 and join the three results.', 'options': [], 'answer': '1065', 'item': 'ESCAPE BADGE', 'need': 'MASTER CARD', 'room': None}]
ROOMS = ["CELLAR","LIBRARY","LABORATORY","WAREHOUSE","VAULT"]

class Game:
    def __init__(self):
        self.save_dir = App.get_running_app().user_data_dir
        os.makedirs(self.save_dir, exist_ok=True)
        self.reset_all()

    def reset_all(self):
        self.level=1; self.lives=3; self.score=0
        self.attempts=0; self.correct=0
        self.inventory=[]; self.secrets=[]; self.achievements=[]
        self.stars=[0]*50; self.won=False; self.game_over=False
        self.time_left=75.0; self.message="Find the clue and escape all 50 rooms!"

    def current(self):
        return LEVELS[self.level-1]

    def room(self):
        return ROOMS[(self.level-1)//10]

    def save(self, slot=1):
        path=os.path.join(self.save_dir, f"escape_slot_{slot}.json")
        data=dict(level=self.level,lives=self.lives,score=self.score,
                  attempts=self.attempts,correct=self.correct,
                  inventory=self.inventory,secrets=self.secrets,
                  achievements=self.achievements,stars=self.stars,won=self.won)
        with open(path,"w",encoding="utf-8") as f: json.dump(data,f)
        self.message=f"SLOT {slot} SAVED"

    def load(self, slot=1):
        path=os.path.join(self.save_dir, f"escape_slot_{slot}.json")
        if not os.path.exists(path):
            self.message=f"SLOT {slot} EMPTY"; return
        with open(path,encoding="utf-8") as f: d=json.load(f)
        self.level=max(1,min(50,int(d.get("level",1))))
        self.lives=max(1,min(3,int(d.get("lives",3))))
        self.score=int(d.get("score",0)); self.attempts=int(d.get("attempts",0))
        self.correct=int(d.get("correct",0)); self.inventory=list(d.get("inventory",[]))
        self.secrets=list(d.get("secrets",[])); self.achievements=list(d.get("achievements",[]))
        self.stars=(list(d.get("stars",[0]*50))+[0]*50)[:50]
        self.won=bool(d.get("won",False)); self.game_over=False
        self.time_left=75.0; self.message=f"SLOT {slot} LOADED"

    def restart_room(self):
        self.time_left=20.0 if self.level in (8,16,24,32,40,48) else 75.0
        self.message="ROOM RESTARTED"

    def check(self, answer):
        if self.won or self.game_over: return
        d=self.current()
        need=d.get("need")
        if need and need not in self.inventory:
            self.message=f"LOCKED — YOU NEED {need}"
            return
        self.attempts += 1
        a=str(answer).strip().upper()
        correct=str(d.get("answer","")).strip().upper()
        if a == correct:
            self.correct += 1
            self.score += 100
            item=d.get("item")
            if item and item not in self.inventory:
                self.inventory.append(item)
                self.message=f"CORRECT! FOUND: {item}"
            else:
                self.message="CORRECT! DOOR UNLOCKED"
            if self.level == 50:
                self.won=True
                self.score += 500
                self.inventory.append("ESCAPE BADGE") if "ESCAPE BADGE" not in self.inventory else None
                self.message="🏆 ESCAPE COMPLETE — ALL 50 ROOMS SOLVED!"
            else:
                self.level += 1
                self.time_left=20.0 if self.level in (8,16,24,32,40,48) else 75.0
        else:
            self.lives -= 1
            self.message=f"WRONG ANSWER — LIVES LEFT: {self.lives}"
            if self.lives <= 0:
                self.game_over=True
                self.message="GAME OVER — PRESS NEW GAME"

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game=Game()
        root=BoxLayout(orientation="vertical",padding=dp(12),spacing=dp(8))
        self.title=Label(text="ESCAPE MYSTERY",font_size=dp(30),bold=True,size_hint_y=None,height=dp(48))
        root.add_widget(self.title)
        self.stats=Label(size_hint_y=None,height=dp(38),font_size=dp(17))
        root.add_widget(self.stats)
        self.room=Label(size_hint_y=None,height=dp(34),font_size=dp(18))
        root.add_widget(self.room)
        self.clue=Label(font_size=dp(20),halign="center",valign="middle")
        self.clue.bind(size=lambda w,v:setattr(w,"text_size",v))
        root.add_widget(self.clue)

        self.answer=TextInput(hint_text="Type answer",multiline=False,font_size=dp(22),
                              size_hint_y=None,height=dp(55),padding=[dp(10),dp(10)])
        root.add_widget(self.answer)

        self.choice_box=GridLayout(cols=2,spacing=dp(8),size_hint_y=None,height=dp(115))
        self.choice_buttons=[]
        for i in range(4):
            b=Button(text="",font_size=dp(18))
            b.bind(on_release=self.choice)
            self.choice_box.add_widget(b); self.choice_buttons.append(b)
        root.add_widget(self.choice_box)

        controls=GridLayout(cols=3,spacing=dp(8),size_hint_y=None,height=dp(58))
        submit=Button(text="UNLOCK",font_size=dp(18)); submit.bind(on_release=self.submit)
        restart=Button(text="RESTART",font_size=dp(18)); restart.bind(on_release=self.restart)
        inv=Button(text="INVENTORY",font_size=dp(18)); inv.bind(on_release=self.inventory)
        controls.add_widget(submit); controls.add_widget(restart); controls.add_widget(inv)
        root.add_widget(controls)

        savebox=GridLayout(cols=4,spacing=dp(6),size_hint_y=None,height=dp(52))
        for n in (1,2,3):
            b=Button(text=f"SAVE {n}"); b.bind(on_release=lambda x,n=n:self.save(n)); savebox.add_widget(b)
        new=Button(text="NEW GAME"); new.bind(on_release=self.new_game); savebox.add_widget(new)
        root.add_widget(savebox)

        self.msg=Label(font_size=dp(16),halign="center",valign="middle")
        self.msg.bind(size=lambda w,v:setattr(w,"text_size",v))
        root.add_widget(self.msg)
        self.add_widget(root)
        Clock.schedule_interval(self.tick,1)
        self.refresh()

    def tick(self,dt):
        if not self.game.game_over and not self.game.won:
            self.game.time_left -= dt
            if self.game.time_left <= 0:
                self.game.time_left=0
                self.game.lives-=1
                if self.game.lives<=0:
                    self.game.game_over=True
                    self.game.message="TIME UP — GAME OVER"
                else:
                    self.game.message=f"TIME UP — LIVES LEFT: {self.game.lives}"
                    self.game.restart_room()
            self.refresh()

    def refresh(self):
        g=self.game; d=g.current()
        self.stats.text=f"Lives: {g.lives}    Score: {g.score}    Time: {int(g.time_left)}s"
        if g.won: self.room.text="🏆 ESCAPED!"
        elif g.game_over: self.room.text="GAME OVER"
        else: self.room.text=f"ROOM {g.level}/50  •  {g.room()}"
        self.clue.text="You escaped!" if g.won else ("Press NEW GAME to start again." if g.game_over else d["clue"])
        self.msg.text=g.message
        opts=d.get("options",[])
        for i,b in enumerate(self.choice_buttons):
            if i<len(opts):
                b.text=str(opts[i]); b.disabled=False
            else:
                b.text=""; b.disabled=True
        self.answer.disabled=g.won or g.game_over

    def choice(self,btn):
        self.answer.text=btn.text
        self.submit()

    def submit(self,*_):
        self.game.check(self.answer.text)
        self.answer.text=""
        self.refresh()

    def restart(self,*_):
        if not self.game.won and not self.game.game_over: self.game.restart_room()
        else: self.game.reset_all()
        self.answer.text=""; self.refresh()

    def new_game(self,*_):
        self.game.reset_all(); self.answer.text=""; self.refresh()

    def inventory(self,*_):
        items=", ".join(self.game.inventory) if self.game.inventory else "EMPTY"
        self.game.message="INVENTORY: "+items
        self.refresh()

    def save(self,n):
        self.game.save(n); self.refresh()

class EscapeMysteryApp(App):
    title="Escape Mystery"
    def build(self):
        Window.clearcolor=(0.03,0.04,0.07,1)
        sm=ScreenManager(); sm.add_widget(MainScreen(name="main")); return sm

if __name__=="__main__":
    EscapeMysteryApp().run()

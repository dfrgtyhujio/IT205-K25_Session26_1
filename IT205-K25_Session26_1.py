class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        return self.get_total_power() > other.get_total_power()


w1 = Warrior("Arthur", 1000, 150, 50)
w2 = Warrior("Lancelot", 900, 180, 10)

print(f"Chiến binh {w1.name} xuất trận!")

if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")
    
    
# Câu 1:
# Lỗi AttributeError xảy ra vì Warrior không gọi hàm khởi tạo của Character,
# nên các thuộc tính name, hp, attack_power chưa được tạo.
# Cú pháp còn thiếu:
# super().__init__(name, hp, attack_power)

# Câu 2:
# Nếu không dùng super(), có thể gọi trực tiếp hàm khởi tạo của lớp cha:
# Character.__init__(self, name, hp, attack_power)
# Tuy nhiên cách này không được khuyến khích vì kém linh hoạt hơn super().

# Câu 3:
# Sau khi sửa lỗi 1, chương trình sẽ báo:
# TypeError: '>' not supported between instances of 'Warrior' and 'Warrior'
# Vì Python không tự biết tiêu chí so sánh hai đối tượng Warrior.

# Câu 4:
# Cần khai báo Dunder Method __gt__(self, other).
# Hàm nhận 2 tham số: self (đối tượng hiện tại) và other (đối tượng cần so sánh).
# Hàm sẽ trả về True nếu self.get_total_power() > other.get_total_power().
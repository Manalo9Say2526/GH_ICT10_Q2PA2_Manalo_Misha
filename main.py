# participation activity
from pyscript import display, document  # type: ignore

def club_member(e):
    document.getElementById('output').innerHTML = ' ' 
    first_name = document.getElementById('firstname').value
    last_name = document.getElementById('lastname').value

    # creating a set to include the new member
    new_member = {f"{first_name} {last_name}"}

    # list of club members per grade level
    grade7 = {'Kylan Gentry', 'Amelie Griffith', 'Franklin Sierra', 'Saoirse Conrad'}
    grade8 = {'Marley Castro', 'Holly Glover', 'Avayah Austin', 'Salvatore Sal'}
    grade9 = {'Jasmeen Kaur', 'Sofia Navarro', 'Blake Pancho', 'Hailey Asis'}
    grade10 = {'Misha Manalo', 'Elise Lim', 'Adri Allas', 'Franchesca Dela Rosa'}

    # combination of all grade levels with the new member
    grade_levels = grade7 | grade8 | grade9 | grade10 | new_member

    # output of combination
    display(grade_levels, target='output')

    # counting of all members
    display(f'The total number of members: {len(grade_levels)}', target='output')

    



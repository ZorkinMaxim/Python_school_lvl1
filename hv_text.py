# text = """
# In tempor lacinia mi a tempus.
# Morbi libero nisi, hendrerit in nibh eu, blandit placerat urna.
# Nullam quis tempor urna.
# Cras tellus diam, porta et sodales sit amet, feugiat eget velit.
# Integer dignissim nisi nunc, in dapibus nisi volutpat ut.
# Mauris feugiat euismod malesuada.
# Fusce eu urna urna.
# Sed vehicula eros sed justo facilisis tincidunt.
# Phasellus porttitor tincidunt velit et tincidunt.
# Sed porttitor tortor eu nunc condimentum, eu porttitor magna varius.
#
# Nunc egestas, purus ac lacinia gravida, urna dolor vestibulum neque, in tincidunt sem risus sed velit.
# Maecenas ornare bibendum lacus in tincidunt.
# Sed vestibulum massa varius nibh porttitor tincidunt.
# Integer id ex a neque pulvinar sagittis quis nec libero.
# Proin vitae elit ultrices metus elementum imperdiet vel non quam.
# Sed dignissim leo eget placerat auctor.
# Donec vulputate molestie dui, ac posuere augue.
# Nunc at suscipit quam.
# Cras erat sem, tincidunt eu varius eu, commodo id sem.
# Ut quis urna ante.
# Proin non ex gravida, feugiat enim vel, finibus nibh.
# Cras ultricies, mi eu molestie mattis, eros sem egestas risus, eget egestas mi enim quis sapien.
# Proin feugiat velit dictum turpis commodo auctor.
# Suspendisse ligula lectus, cursus eget tincidunt quis, dignissim at augue.
# Vestibulum ut est vitae tortor ornare egestas.
#
# Mauris lobortis ac quam ut viverra.
# Cras venenatis, lacus quis cursus auctor, mauris sapien cursus orci, in ultrices neque libero ac ex.
# Praesent eleifend enim nisl, in ornare ante mollis at.
# Sed ac consequat turpis, id semper diam.
# Nunc sit amet auctor est, quis cursus lectus.
# Suspendisse quis suscipit tellus.
# Morbi elementum mattis ornare.
# Nunc posuere arcu non urna pulvinar, eget tempus massa pharetra.
# Sed at ipsum interdum, facilisis nisi non, aliquam erat.
# Aliquam aliquet volutpat semper.
# Integer a tortor ac quam tincidunt fermentum pretium sed est.
# Pellentesque at ligula vitae ipsum blandit venenatis ut sit amet velit.
# Suspendisse congue a leo eget rhoncus.
# Fusce velit nunc, molestie vitae purus ac, feugiat sodales nulla."""
#
# index = 0
# while index < len(text):
#     print(text[index], end="")
#
#     if text[index] == ".":
#         print("", end=" ")
#         index += 1
#     index += 1


text = """"
In tempor lacinia mi a tempus. Morbi libero nisi, hendrerit in nibh eu, blandit placerat urna. Nullam quis tempor urna. Cras tellus diam, porta et sodales sit amet, feugiat eget velit. Integer dignissim nisi nunc, in dapibus nisi volutpat ut. Mauris feugiat euismod malesuada. Fusce eu urna urna. Sed vehicula eros sed justo facilisis tincidunt. Phasellus porttitor tincidunt velit et tincidunt. Sed porttitor tortor eu nunc condimentum, eu porttitor magna varius. 
Nunc egestas, purus ac lacinia gravida, urna dolor vestibulum neque, in tincidunt sem risus sed velit. Maecenas ornare bibendum lacus in tincidunt. Sed vestibulum massa varius nibh porttitor tincidunt. Integer id ex a neque pulvinar sagittis quis nec libero. Proin vitae elit ultrices metus elementum imperdiet vel non quam. Sed dignissim leo eget placerat auctor. Donec vulputate molestie dui, ac posuere augue. Nunc at suscipit quam. Cras erat sem, tincidunt eu varius eu, commodo id sem. Ut quis urna ante. Proin non ex gravida, feugiat enim vel, finibus nibh. Cras ultricies, mi eu molestie mattis, eros sem egestas risus, eget egestas mi enim quis sapien. Proin feugiat velit dictum turpis commodo auctor. Suspendisse ligula lectus, cursus eget tincidunt quis, dignissim at augue. Vestibulum ut est vitae tortor ornare egestas. 
Mauris lobortis ac quam ut viverra. Cras venenatis, lacus quis cursus auctor, mauris sapien cursus orci, in ultrices neque libero ac ex. Praesent eleifend enim nisl, in ornare ante mollis at. Sed ac consequat turpis, id semper diam. Nunc sit amet auctor est, quis cursus lectus. Suspendisse quis suscipit tellus. Morbi elementum mattis ornare. Nunc posuere arcu non urna pulvinar, eget tempus massa pharetra. Sed at ipsum interdum, facilisis nisi non, aliquam erat. Aliquam aliquet volutpat semper. Integer a tortor ac quam tincidunt fermentum pretium sed est. Pellentesque at ligula vitae ipsum blandit venenatis ut sit amet velit. Suspendisse congue a leo eget rhoncus. Fusce velit nunc, molestie vitae purus ac, feugiat sodales nulla.
"""
index = 0
while index < len(text):
    print(text[index], end="")

    if text[index] == "." and text[index+1] == " ":
        print()
        index += 1
    index += 1
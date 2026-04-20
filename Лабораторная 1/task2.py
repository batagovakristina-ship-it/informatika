# TODO Найдите количество книг, которое можно разместить на дискете
memory_size = 1.44
bytes_in_mb = 1024 * 1024
page = 100
row = 50
symbol_count = 25
simbol = 4

# Найдем дискету в байтах
memory = memory_size * bytes_in_mb
# Найдём объём, который символы занимают в книге
size = simbol * symbol_count * row * page
# Найдём количество книг, которые можно поместить на дискету
count = int(memory // size)

print("Количество книг, помещающихся на дискету:", count)

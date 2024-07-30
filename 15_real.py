def compute_lattice_paths(grid_size):
    # Створюємо двовимірний масив для зберігання результатів
    dp = [[0] * (grid_size + 1) for _ in range(grid_size + 1)]


    # Ініціалізуємо значення у крайніх точках
    for i in range(grid_size + 1):
        dp[i][0] = dp[0][i] = 1

    # Заповнюємо масив значеннями залежно від попередніх значень
    for i in range(1, grid_size + 1):
        for j in range(1, grid_size + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Повертаємо кількість можливих шляхів

    return dp[grid_size][grid_size]

grid_size = 20
result = compute_lattice_paths(grid_size)
print('result=',result)


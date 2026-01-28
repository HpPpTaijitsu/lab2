import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """Основная функция для запуска лабораторной работы."""
    print("=" * 60)
    print("Лабораторная работа: Исследование поиска в ширину (BFS)")
    print("=" * 60)
    
    while True:
        print("\nВыберите задание:")
        print("1. Пример BFS на простом графе")
        print("2. Задача: Подсчет островов в матрице")
        print("3. Задача: Поиск пути в лабиринте")
        print("4. Задача: Поиск пути в графе Румынии")
        print("5. Сравнение с ручным решением")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '1':
            from examples.bfs_example import run_example
            run_example()
        
        elif choice == '2':
            from tasks.islands import test_islands
            test_islands()
        
        elif choice == '3':
            from tasks.maze import test_maze
            test_maze()
        
        elif choice == '4':
            from tasks.romania_graph import find_shortest_path
            find_shortest_path('Arad', 'Bucharest')
        
        elif choice == '5':
            from tasks.romania_graph import compare_with_manual
            compare_with_manual()
        
        elif choice == '0':
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
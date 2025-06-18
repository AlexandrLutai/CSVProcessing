from csv_processor.args import parse_args, parse_condition
from csv_processor.csv_reader import read_csv
from csv_processor.filter import filter_data
from csv_processor.aggregate import aggregate_column
from csv_processor.output import print_table
import sys

def main():
    try:
        args = parse_args()
        data = read_csv(args.file)
        if not getattr(args, "command", None):
            
            print_table(data)
            return
        if args.command == "where":
            column, operator, value = parse_condition(args.condition)
            filtered = filter_data(data, column, operator, value)
            print_table(filtered)
        elif args.command == "aggregate":
            column, operator, value = parse_condition(args.condition)
            if operator != "=":
                print("Для агрегации используйте только оператор '=' (например: rating=avg)")
                sys.exit(1)
            result = aggregate_column(data, column, value)
            print_table([{"column": column, "operation": value, "result": result}])
        else:
            print("Неизвестная команда.")
            sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


from csv_processor.args import parse_args, parse_condition, parse_order_by
from csv_processor.csv_reader import read_csv
from csv_processor.filter import filter_data
from csv_processor.aggregate import aggregate_column
from csv_processor.output import print_table
from csv_processor.order_by import order_by
import sys

def main():
    try:
        args = parse_args()
        data = read_csv(args.file)

        
        order_column, order_direction = None, None
        if hasattr(args, "order_by") and args.order_by:
            order_column, order_direction = parse_order_by(args.order_by)

        if not getattr(args, "command", None):
            sorted_data = order_by(data, order_column, order_direction)
            print_table(sorted_data)
            return

        if args.command == "where":
            column, operator, value = parse_condition(args.condition)
            filtered = filter_data(data, column, operator, value)
            sorted_data = order_by(filtered, order_column, order_direction)
            print_table(sorted_data)
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


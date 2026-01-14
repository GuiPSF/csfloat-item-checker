from services.items_service import get_items
from data.filters import build_filter, build_filtered_df


def main() -> None:
    df = get_items()

    item_name = input("Please provide the item name that you want to search for: ")

    mask = build_filter(df, item_name)
    filtered_df = build_filtered_df(df, mask)

    print(filtered_df)


if __name__ == "__main__":
    main()

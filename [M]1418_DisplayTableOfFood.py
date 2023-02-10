class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # Loop through orders and create a hashmap that keep track number per items using Counter

        food_list = set()

        order_map = collections.defaultdict(list)
        for order in orders:
            order_map[order[1]].append(order[2])
            food_list.add(order[2])
        order_map = {k:collections.Counter(v) for (k,v) in order_map.items()}

        sorted_map = sorted(order_map.items(), key=lambda x: int(x[0]))
        food_list = sorted(list(food_list))
        food_list.insert(0, "Table")
        output = [food_list]

        for table, order in sorted_map:
            table_order = [table]
            for food in food_list[1:]:
                table_order.append(str(order[food]))
            output.append(table_order)

        return output

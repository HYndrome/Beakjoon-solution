i_n = int(input())
ls_city_budget = list(map(int, input().split()))
i_total_budget = int(input())


def city_budget_divider(budgets, total_budget):
    budgets.sort()
    ls_result = []

    def budget_allocator(target):
        nonlocal budgets
        nonlocal total_budget
        budget_sum = 0
        for budget in budgets:
            if budget <= target:
                budget_sum += budget
            else:
                budget_sum += target
        if budget_sum <= total_budget:
            return True
        else:
            return False
    
    def bi_search(start, end):
        if start <= end:
            mid = (start + end) // 2
            if budget_allocator(mid):
                ls_result.append(mid)
                bi_search(mid + 1, end)
            else:
                bi_search(start, mid - 1)
    
    bi_search(total_budget // len(budgets), budgets[-1])

    return max(ls_result)

if sum(ls_city_budget) <= i_total_budget:
    print(max(ls_city_budget))
else:
    print(city_budget_divider(ls_city_budget, i_total_budget))
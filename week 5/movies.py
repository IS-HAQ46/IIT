movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0,
    "Spiderman":17.0
}

purchases = []
while True:
    title = input("Enter movie title (or 'done' to finish): ")
    if title.lower() == "done":
        break

    if title not in movies:
        print("Movie not found. Available movies:", ", ".join(movies.keys()))
        continue

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    price_each = movies[title]

    line_total = qty * price_each
    if qty >= 4:  
        line_total *= 0.9
        print("Applied 10% group discount!")

    purchases.append((title, qty, price_each, line_total))

print("\n--- Receipt ---")
grand_total = 0
for title, qty, price_each, line_total in purchases:
    print(f"{title:15} x{qty:<2} @ ${price_each:.2f} = ${line_total:.2f}")
    grand_total += line_total

is_member = input("Do you have a member code? (y/n): ").strip().lower() == "y"
if is_member:
    grand_total *= 0.95
    print("Applied 5% member discount!")

print(f"Grand Total: ${grand_total:.2f}")

tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each, line_total in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0) + line_total

print("\n--- Sales Summary ---")
for title in movies:
    tickets = tickets_by_movie.get(title, 0)
    revenue = revenue_by_movie.get(title, 0.0)
    print(f"{title:15} Tickets: {tickets:<3}  Revenue: ${revenue:.2f}")

top_title = None
top_qty = -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty
print(f"\nTop seller: {top_title} with {top_qty} tickets")

sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
print("\nMovies sorted by revenue:")
for title, revenue in sorted_by_rev:
    print(f"{title:15} ${revenue:.2f}")

if purchases:
    total_tickets = sum(qty for _, qty, _, _ in purchases)
    avg_tickets = total_tickets / len(purchases)
    print(f"\nAverage tickets per purchase: {avg_tickets:.2f}")
else:
    print("\nNo purchases made.")
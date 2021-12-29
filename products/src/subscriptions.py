def format_subscriptions_to_interface(stripe_subscriptions):
    formatted_price_subscriptions_list = []
    for stripe_subscription in stripe_subscriptions:
        formatted_price_subscriptions_list.append(
            {
                'id': stripe_subscription.id,
                'name': stripe_subscription.name,
                'price': stripe_subscription.price,
                'price_to_interface': float(stripe_subscription.price) / 100,
                'stripe_product_id': stripe_subscription.stripe_product_id,
                'stripe_product_mode': stripe_subscription.stripe_product_mode
            }
        )
    return formatted_price_subscriptions_list

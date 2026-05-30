def apply_discount(price, discount):
  if not isinstance(price, (float,int)):
    return "The price should be a number"
  elif not isinstance(discount, (float,int)):
    return "The discount should be a number"
  elif price <= 0:
    return "The price should be greater than 0"
  elif discount < 0 or discount > 100:
    return "The discount should be between 0 and 100"
  else:
    discount_amount = (discount / 100) * price
    return price - discount_amount

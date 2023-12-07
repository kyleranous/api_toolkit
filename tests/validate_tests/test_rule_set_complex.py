"""
Complex test of the RuleSet class
"""

from api_toolkit.validate import RuleSet
from api_toolkit.validate import Rules as r


def test_complex_ruleset():
    """
    Test that a complex rule set with payload that is
    missing non-required fields still passes
    """
    test_payload = {
        "shop": "storefront-catalog-en",
        "shop_locale": "en-US",
        "external_id": "9999999",
        "channel_type": "web",
        "channel_name": "USC",
        "currency": "USD",
        "customer_name": "Jason Juke",
        "customer_email": "JasonJuke@fakemail.com",
        "customer_locale": "EN-US",
        "external_customer_id": "123456789",
        "placed_at": "2023-12-06T18:27:18-05:00",
        "price_method": "tax_excluded",
        "shipping_address": {
            "first_name": "Jason",
            "last_name": "Juke",
            "country": "US",
            "zip_code": "27587",
            "city": "Georgetown",
            "state": "CO",
            "address_line_1": "5508 Via Lombardia Plz",
            "address_line_2": "",
            "phone": "(999) 999-9999"
        },
        "billing_address": {
            "first_name": "Jason",
            "last_name": "Juke",
            "country": "US",
            "zip_code": "27587",
            "city": "Georgetown",
            "state": "CO",
            "address_line_1": "5508 Via Lombardia Plz",
            "address_line_2": "",
            "phone": "(999) 999-9999"
        },
        "shipments": [
            {
                "items": [
                    {
                        "external_item_id": "40240461643845",
                        "product_id": "MWU2302-WRK-XL",
                        "item_tax_lines": [
                            {
                                "amount": 2.13,
                                "rate": 0.0475,
                                "name": "NC STATE TAX"
                            },
                            {
                                "amount": 0.9,
                                "rate": 0.02,
                                "name": "NC COUNTY TAX"
                            },
                            {
                                "amount": 0.22,
                                "rate": 0.005,
                                "name": "NC SPECIAL TAX"
                            }
                        ],
                        "price": {
                            "item_price": 64,
                            "item_list_price": 64,
                            "item_tax_lines": [
                                {
                                    "amount": 2.13,
                                    "rate": 0.0475,
                                    "name": "NC STATE TAX"
                                },
                                {
                                    "amount": 0.9,
                                    "rate": 0.02,
                                    "name": "NC COUNTY TAX"
                                },
                                {
                                    "amount": 0.22,
                                    "rate": 0.005,
                                    "name": "NC SPECIAL TAX"
                                }
                            ],
                            "item_discount_info": [
                                {
                                    "type": "percentage",
                                    "original_value": 30,
                                    "price_adjustment": 19.2,
                                    "discount_ref": "SALE30",
                                    "coupon_code": "",
                                    "description": ""
                                }
                            ],
                            "item_order_discount_info": []
                        },
                        "extended_attributes": [
                            {
                                "name": "is_gift_card",
                                "value": "False"
                            },
                            {
                                "name": "requires_shipping",
                                "value": "True"
                            },
                            {
                                "name": "external_item_id",
                                "value": "12773457592389"
                            }
                        ]
                    },
                    {
                        "external_item_id": "40383447171141",
                        "product_id": "MWU2322-MIB-XL",
                        "item_tax_lines": [
                            {
                                "amount": 1.96,
                                "rate": 0.0475,
                                "name": "NC STATE TAX"
                            },
                            {
                                "amount": 0.83,
                                "rate": 0.02,
                                "name": "NC COUNTY TAX"
                            },
                            {
                                "amount": 0.21,
                                "rate": 0.005,
                                "name": "NC SPECIAL TAX"
                            }
                        ],
                        "price": {
                            "item_price": 59,
                            "item_list_price": 59,
                            "item_tax_lines": [
                                {
                                    "amount": 1.96,
                                    "rate": 0.0475,
                                    "name": "NC STATE TAX"
                                },
                                {
                                    "amount": 0.83,
                                    "rate": 0.02,
                                    "name": "NC COUNTY TAX"
                                },
                                {
                                    "amount": 0.21,
                                    "rate": 0.005,
                                    "name": "NC SPECIAL TAX"
                                }
                            ],
                            "item_discount_info": [
                                {
                                    "type": "percentage",
                                    "original_value": 30,
                                    "price_adjustment": 17.7,
                                    "discount_ref": "SALE30",
                                    "coupon_code": "",
                                    "description": ""
                                }
                            ],
                            "item_order_discount_info": []
                        },
                        "extended_attributes": [
                            {
                                "name": "is_gift_card",
                                "value": "False"
                            },
                            {
                                "name": "requires_shipping",
                                "value": "True"
                            },
                            {
                                "name": "external_item_id",
                                "value": "12773457625157"
                            }
                        ]
                    },
                    {
                        "external_item_id": "40022269657157",
                        "product_id": "MWS2322-GSG-XL",
                        "item_tax_lines": [
                            {
                                "amount": 2.13,
                                "rate": 0.0475,
                                "name": "NC STATE TAX"
                            },
                            {
                                "amount": 0.9,
                                "rate": 0.02,
                                "name": "NC COUNTY TAX"
                            },
                            {
                                "amount": 0.22,
                                "rate": 0.005,
                                "name": "NC SPECIAL TAX"
                            }
                        ],
                        "price": {
                            "item_price": 64,
                            "item_list_price": 64,
                            "item_tax_lines": [
                                {
                                    "amount": 2.13,
                                    "rate": 0.0475,
                                    "name": "NC STATE TAX"
                                },
                                {
                                    "amount": 0.9,
                                    "rate": 0.02,
                                    "name": "NC COUNTY TAX"
                                },
                                {
                                    "amount": 0.22,
                                    "rate": 0.005,
                                    "name": "NC SPECIAL TAX"
                                }
                            ],
                            "item_discount_info": [
                                {
                                    "type": "percentage",
                                    "original_value": 30,
                                    "price_adjustment": 19.2,
                                    "discount_ref": "SALE30",
                                    "coupon_code": "",
                                    "description": ""
                                }
                            ],
                            "item_order_discount_info": []
                        },
                        "extended_attributes": [
                            {
                                "name": "is_gift_card",
                                "value": "False"
                            },
                            {
                                "name": "requires_shipping",
                                "value": "True"
                            },
                            {
                                "name": "external_item_id",
                                "value": "12773457657925"
                            }
                        ]
                    }
                ],
                "shipping_option": {
                    "service_level_identifier": "FedEx - Home Delivery",
                    "price": 0,
                    "tax": 0
                }
            }
        ],
        "payments": [
            {
                "processor": "shopify",
                "correlation_ref": "6507745869893",
                "type": "captured",
                "amount": 140.4,
                "method": "credit_card",
                "processed_at": "2023-12-06T18:27:16-05:00",
                "metadata": {
                    "avs_result_code": "Y",
                    "cvv_result_code": "M",
                    "credit_card_number": "•••• •••• •••• 9999",
                    "credit_card_company": "Visa",
                    "buyer_action_info": ""
                }
            }
        ],
        "extended_attributes": [
            {
                "name": "returnly_exchange",
                "value": "False"
            },
            {
                "name": "external_order_id",
                "value": "1829017"
            },
            {
                "name": "order_id",
                "value": "5174588637253"
            },
            {
                "name": "ext_channel_name",
                "value": "USC"
            },
            {
                "name": "is_historical",
                "value": "False"
            },
            {
                "name": "order_memo",
                "value": ""
            }
        ],
        "notification_blacklist": [
            "shipment_dispatched",
            "order_cancelled",
            "refund_note_created"
        ],
        "ip_address": "127.0.0.1"
    }

    rule_set = create_order_validation_ruleset()
    rule_set.test_dict = test_payload

    assert bool(rule_set)
    assert not rule_set.errors

def create_order_validation_ruleset():
    """
    Build and return the validation dictionary for the create_order API
    """
    # Define Parent Validation Ruleset
    validation_dict = {
        'external_id': [r.required(), r.is_type(str), r.length(min=1, max=64)],
        'shop': [r.required(), r.is_type(str), r.length(min=1, max=128)],
        'channel_type': [r.required(), r.is_type(str), r.is_in('web', 'mobile', 'store')],
        'channel_name': [r.required(), r.is_type(str), r.length(min=1, max=64)],
        'store_id': [r.is_type(str), r.length(max=256)],
        'associate_id': [r.is_type(str), r.length(max=256)],
        'customer_name': [r.is_type(str), r.length(max=128)],
        'customer_email': [r.is_type(str), r.email(), r.length(max=64)],
        'shop_locale': [r.required(), r.is_type(str), r.length(min=1, max=128)],
        'customer_language': [r.is_type(str), r.length(max=2)],
        'external_customer_id': [r.is_type(str), r.length(max=64)],
        'placed_at': [r.is_type(str)],
        'ip_address': [r.is_type(str)],
        'shipping_address': [r.is_type(dict), build_address_validation_ruleset()],
        'shipments': [r.required(),
                      r.is_type(list),
                      [build_shipment_validation_ruleset()]
                     ],
        'extended_attributes': [r.is_type(list),
                                [build_extended_attributes_validation_ruleset()]],
        'billing_address': [r.is_type(dict), build_address_validation_ruleset()],
        'payments': [r.is_type(list), [build_payment_validation_dict()]],
        'price_method': [r.is_type(str), r.is_in('tax_included', 'tax_excluded')],
        'is_preconfirmed': [r.is_type(bool)],
        'is_fulfilled': [r.is_type(bool)],
        'is_offline': [r.is_type(bool)],
        'is_historical': [r.is_type(bool)],
        'notification_blacklist': [r.is_type(list), [r.is_type(str)]],
        'currency': [r.required(), r.is_type(str), r.is_in("USD")]
    }
    order_validation_ruleset = RuleSet(validation_dict)
    return order_validation_ruleset

def build_address_validation_ruleset():
    """
    Build the validation ruleset for address validation
    """
    # Define the ruleset for the address validation
    str_32_char = [r.is_type(str), r.length(max=32)]
    str_64_char = [r.is_type(str), r.length(max=64)]
    address_validation_dict = {
        'title': str_32_char,
        'suffix': str_32_char,
        'salutation': str_32_char,
        'first_name': str_64_char,
        'last_name': str_64_char,
        'country': [r.required(), r.is_type(str), r.length(min=2, max=2)],
        'zip_code': str_32_char,
        'city': str_64_char,
        'state': str_32_char,
        'address_line_1': [r.required(), r.is_type(str), r.length(min=1, max=128)],
        'address_line_2': [r.is_type(str), r.length(max=256)],
        'phone': [r.is_type(str), r.length(max=128)]
    }
    address_rule_set = RuleSet(address_validation_dict)

    return address_rule_set

def build_shipment_validation_ruleset():
    """
    Build the shipment validation ruleset for create_order API
    """
    # Define Shipments Validation Ruleset
    shipment_validation = {
        'items': [r.required(),
                    r.is_type(list),
                    [r.is_type(dict),
                    build_item_validation_ruleset()]
                ],
        'shipping_option': [r.required(), build_shipping_option_validation_ruleset()],
    }
    shipment_ruleset = RuleSet(shipment_validation)
    return shipment_ruleset

def build_item_validation_ruleset():
    """
    Build the item validation ruleset for create_order API
    """
    # Define Item Validation Dict
    item_validation_dict = {
        'external_item_id': [r.required(), r.is_type(str), r.length(min=1, max=64)],
        'product_id': [r.required(), r.is_type(str), r.length(min=1, max=64)],
        'price': [r.required(), r.is_type(dict), build_price_validation_ruleset()],
        'gift_wrapping': [r.is_type(bool)],
        'extended_attributes': [r.is_type(list),
                                [build_extended_attributes_validation_ruleset()]
                                ]
    }

    item_validation_ruleset = RuleSet(item_validation_dict)
    return item_validation_ruleset

def build_price_validation_ruleset():
    """
    Build the price validation ruleset used in the item validation ruleset
    """
    # Define Price Validation Dict
    price_validation_dict = {
        'item_price': [r.required(), r.is_type(int, float)],
        'item_list_price': [r.required(), r.is_type(int, float)],
        'item_tax_lines': [r.required(),
                            r.is_type(list),
                            [build_item_tax_lines_validation_ruleset()]
                            ],
        'item_order_discount_info': [r.is_type(list),
                                        [build_order_discount_validation_ruleset()]],
        'pricebook': [r.is_type(str), r.length(max=64)],
        'group_ref': [r.is_type(str), r.length(max=64)]
    }

    price_validation_ruleset = RuleSet(price_validation_dict)
    return price_validation_ruleset

def build_order_discount_validation_ruleset():
    """
    Build the order discount validation ruleset used in the price validation ruleset
    """
    # Define Order Discount Validation Dict
    order_discount_validation_dict = {
        'discount_ref': [r.required(), r.is_type(str), r.length(max=256)],
        'coupon_code': [r.is_type(str), r.length(max=64)],
        'description': [r.is_type(str), r.length(max=1024)],
        'type': [r.required(), r.is_type(str), r.is_in('fixed')],
        'original_value': [r.required(), r.is_type(int, float), r.Min(0)],
        'price_adjustment': [r.required(), r.is_type(int, float), r.Min(0)]
    }
    order_discount_validation_ruleset = RuleSet(order_discount_validation_dict)
    return order_discount_validation_ruleset

def build_item_tax_lines_validation_ruleset():
    """
    Build the tax lines validation ruleset used in the price validation ruleset
    """
    # Define Item Tax Lines Validation Dict
    item_tax_lines_validation_dict = {
        'amount': [r.required(), r.is_type(int, float)],
        'rate': [r.required(), r.is_type(float), r.Min(0), r.Max(1)],
        'name': [r.required(), r.is_type(str)],
        'country_code': [r.is_type(str), r.length(max=2)]
    }
    item_tax_lines_validation_ruleset = RuleSet(item_tax_lines_validation_dict)
    return item_tax_lines_validation_ruleset

def build_extended_attributes_validation_ruleset():
    """
    Build the validation ruleset for extended attributes
    """
    # Define Extended Attributes Validation Dict
    extended_attributes_validation_dict = {
        'name': [r.required(), r.is_type(str), r.length(min=1, max=100)],
        'value': [r.required(), r.is_type(str), r.length(max=8192)]
    }
    extended_attributes_validation_ruleset = RuleSet(extended_attributes_validation_dict)
    return extended_attributes_validation_ruleset

def build_shipping_option_validation_ruleset():
    """
    Build the validation ruleset for shippiing option validation
    """
    # Define Shipping Options Validation Dict
    shipping_options_validation_dict = {
        'service_level_identifier': [r.required(), r.is_type(str), r.length(min=1, max=64)],
        'price': [r.required(), r.is_type(int, float), r.Min(0)],
        'tax': [r.required(), r.is_type(int, float), r.Min(0)],
        'discount_info': [r.is_type(list), build_order_discount_validation_ruleset()],
        'routing_strategy': [r.is_type(dict), build_routing_strategy_validation_ruleset()]
    }
    shipping_options_validation_ruleset = RuleSet(shipping_options_validation_dict)
    return shipping_options_validation_ruleset

def build_routing_strategy_validation_ruleset():
    """
    Build the validation ruleset for routing strategy validation
    """
    # Define Routing Strategy Validation Dict
    routing_strategy_validation_dict = {
        'strategy': [r.required(), r.is_type(str)]
    }
    routing_strategy_validation_ruleset = RuleSet(routing_strategy_validation_dict)
    return routing_strategy_validation_ruleset

def build_payment_validation_dict():
    """
    Build the payment validation ruleset for order validation
    """
    # Define Payment Validation Dict
    payment_validation_dict = {
        'type': [r.required(), r.is_type(str), r.is_in('authorized', 'captured')],
        'amount': [r.required(), r.is_type(int, float), r.Min(0.01)],
        'method': [r.required(), r.is_type(str), r.length(min=1, max=64)],
        'wallet': [r.is_type(str), r.length(min=1,max=64)],
        'processed_at': [r.required(), r.is_type(str)],
        'metadata': [r.is_type(dict), r.length(max=100)],
        'processor': [r.required(), r.is_type(str), r.length(min=1, max=32)],
        'correlation_ref': [r.required(), r.is_type(str), r.length(min=1, max=128)]
    }
    payment_validation_ruleset = RuleSet(payment_validation_dict)
    return payment_validation_ruleset

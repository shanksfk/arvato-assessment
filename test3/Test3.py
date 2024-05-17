"""
    FILL IN THIS CODE

    (you're allowed to create new interfaces, classes etc. as much as you want!)
    such that given an Address, it should be possible to return the formatted address lines
    depending on the country address format.

    For example:
    <li>US Address Format
    <pre>
      street
      state, pobox
      US
    </pre>
    <li>German Address Format
    <pre>
      street, pobox
      state, DE
    </pre>

    NOTE that it should be as easy as possible to add any number of new address lines format
    e.g. for Malaysia, Thailand etc. in the near future

    @param address the address
    @return formatted address lines
"""


class Address:
    def __init__(self, country_code: str, street: str, state: str, po_box: str = None):
        self.country_code = country_code
        self.street = street
        self.state = state
        self.po_box = po_box

    def format_address(self):
        address_formats = {
            "US": lambda addr: [addr.street, f"{addr.state}, {addr.po_box}", "US"],
            "DE": lambda addr: [f"{addr.street}, {addr.po_box}", f"{addr.state}, DE"]
        }

        if self.country_code in address_formats:
            return address_formats[self.country_code](self)
        else:
            return [f"No address format defined for {self.country_code}"]


if __name__ == "__main__":
    usa_address = Address(country_code="US", street="street", state="state", po_box="PoBox")
    print("US Address")
    print("----------")
    for address_line in usa_address.format_address():
        print(address_line)

    german_address = Address(country_code="DE", street="street", state="state", po_box="PoBox")
    print("\nDE Address")
    print("----------")
    for address_line in german_address.format_address():
        print(address_line)

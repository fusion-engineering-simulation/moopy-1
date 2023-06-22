class UserObjects:
    def __init__(self, name="UserObjects"):
        self.name = name
        self.sections = []

    def add_section(self, section_name, **kwargs):
        section = {section_name: kwargs}
        self.sections.append(section)

    def __str__(self):
        string = f"[{self.name}]\n"
        for section in self.sections:
            section_name = list(section.keys())[0]
            string += f"  [{section_name}]\n"
            attributes = section[section_name]
            for key in attributes.keys():
                string += f"    {key} = {attributes[key]}\n"
            string += "  []\n"
        string += "[]\n"
        return string

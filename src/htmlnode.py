from pydoc import html


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props == None or self.props == {}:
            return ""
        prop_list = []
        for p in self.props:
            to_add = (f'{p}="{self.props[p]}"')
            prop_list.append(to_add)
        final = ""
        for pl in prop_list:
            final = final + " " + pl
        return final

    def __repr__(self) -> str:
        return (f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value!")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return (f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})")

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag!")
        if self.children == None:
            raise ValueError("No children!")
        the_children = ""
        for child in self.children:
            html_string = child.to_html()
            the_children = the_children + html_string

        return (f'<{self.tag}{self.props_to_html()}>{the_children}</{self.tag}>')

import copy
from distutils.sysconfig import PREFIX
from sys import prefix
from docutils import nodes
from docutils.statemachine import StringList
from sphinx import addnodes
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging
from sphinx.util.typing import OptionSpec
from typing import TYPE_CHECKING, Any, Dict, List, cast
from docutils.nodes import Element, Node

logger = logging.getLogger(__name__)

PREFIX = ['A', 'B', 'C', 'D', 'E']

POSITIONS = {
    "default": [0, 1, 2, 3, 4],
    4: [0, 2, 1, 3],
    5: [0, 2, 4, 1, 3]
}

def get_columns(choices):
    if len(choices) < 3:
        return 1
    for choice in choices:
        if len(choice) > 35:
            return 1
    return 2
        
def get_columns_and_updated_choices(choices):
    columns = get_columns(choices)
    prefix = PREFIX
    if columns == 2:
        positions = POSITIONS.get(len(choices))
        choices = [choices[p] for p in positions]
        prefix = [prefix[p] for p in positions]
    new_choices = [f'- [{o}] {c.strip("-").strip()}' for o, c in zip(prefix, choices)]
    return columns, new_choices

class MCQ(SphinxDirective):
    """
    Directive for a list that gets compacted horizontally.
    """
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec: OptionSpec = {
        'question': str,
        'year': str,
    }

    def run(self) -> List[Node]:
        # comma separated options
        
        return_list = []
        if len(self.content.data):
            if len(self.content.data) == 1:
                choices = self.content.data[0].strip('-').split(',')
                choices = [f'- {c.strip()}' for c in choices]
                self.content.data = [f'{c.strip()}' for c in choices]

            no_of_choices = len(self.content.data)
            if no_of_choices > 5:
                logger.warning('.. max 5 choices are allowed',
                               location=(self.env.docname, self.lineno))
                return []
            ncolumns, new_list = get_columns_and_updated_choices(self.content.data)
            updated_content = copy.deepcopy(self.content)
            updated_content.data = new_list
            # answer = self.options.get('answer', "No Answer")
            node = nodes.paragraph()
            node.document = self.state.document
            self.content = updated_content
            self.state.nested_parse(self.content, self.content_offset, node)
            if len(node.children) != 1 or not isinstance(node.children[0],
                                                         nodes.bullet_list):
                logger.warning('.. mcq content is not a list',
                               location=(self.env.docname, self.lineno))
                return []
            fulllist = node.children[0]
            # create a hlist node where the items are distributed
            npercol, nmore = divmod(len(fulllist), ncolumns)
            index = 0
            newnode = addnodes.hlist()
            newnode['ncolumns'] = str(ncolumns)
            for column in range(ncolumns):
                endindex = index + ((npercol + 1) if column < nmore else npercol)
                bullet_list = nodes.bullet_list()
                bullet_list += fulllist.children[index:endindex]
                newnode += addnodes.hlistcol('', bullet_list)
                index = endindex

            return_list += [newnode]

        question = self.options.get('question', '')
        year = self.options.get('year', '')
        if question.strip():
            q_cont = nodes.container()
            self.content.data = [question]
            self.state.nested_parse(self.content, self.content_offset, q_cont)
            return_list = [q_cont] + return_list

        if year.strip():
            y_cont = nodes.footnote()
            self.content.data = [f"[{year}]"]
            self.state.nested_parse(self.content, self.content_offset, y_cont)
            return_list += [y_cont]

        return return_list

def setup(app):
    app.add_directive('mcq', MCQ)
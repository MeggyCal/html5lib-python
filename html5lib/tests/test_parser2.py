from __future__ import absolute_import, division, unicode_literals

import io

from . import support  # noqa

from html5lib.constants import namespaces
from html5lib import parse


# tests that aren't autogenerated from text files
def test_assertDoctypeCloneable():
    doc = parse('<!DOCTYPE HTML>', treebuilder="dom")
    assert doc.cloneNode(True) is not None


def test_line_counter():
    # http://groups.google.com/group/html5lib-discuss/browse_frm/thread/f4f00e4a2f26d5c0
    assert parse("<pre>\nx\n&gt;\n</pre>") is not None


def test_namespace_html_elements_0_dom():
    doc = parse("<html></html>",
                treebuilder="dom",
                namespaceHTMLElements=True)
    assert doc.childNodes[0].namespaceURI == namespaces["html"]


def test_namespace_html_elements_1_dom():
    doc = parse("<html></html>",
                treebuilder="dom",
                namespaceHTMLElements=False)
    assert doc.childNodes[0].namespaceURI is None


def test_namespace_html_elements_0_etree():
    doc = parse("<html></html>",
                treebuilder="etree",
                namespaceHTMLElements=True)
    assert doc.tag == "{%s}html" % (namespaces["html"],)


def test_namespace_html_elements_1_etree():
    doc = parse("<html></html>",
                treebuilder="etree",
                namespaceHTMLElements=False)
    assert doc.tag == "html"


def test_unicode_file():
    assert parse(io.StringIO("a")) is not None

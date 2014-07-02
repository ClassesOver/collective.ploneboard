# -*- coding: UTF-8 -*-
from plone.app.textfield import RichText
from plone.directives import form
from zope import schema
from zope.interface import Interface
from collective.ploneboard import _
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IContextSourceBinder
from five import grok


@grok.provider(IContextSourceBinder)
def possibleCategories(context):
    terms = []
    category = list(set(context.cats))
    for category_i in category:
        terms.append(SimpleVocabulary.createTerm(
            str(category_i),
            str(category_i),
            str(category_i)))
    return SimpleVocabulary(terms)


class IMessageboard(form.Schema):
    category = schema.Text(
        title=_(u"Categories"),
        description=_(
            u"Enter the categories you want to have available for topics," +
            "one category on each line."
            ),
        required=False,
        )


class ITopic(form.Schema):
    category = schema.List(
        title=_(u"Category"),
        description=_(u"Choose to tag your Topic"),
        value_type=schema.Choice(
            title=_(u"Ssup"),
            source=possibleCategories,
            ),
        required=False,
        )


class IConversation(form.Schema):
    """
    """
    text = RichText(
        title=_(u"Text"),
        required=True,
        )


class IPloneboardLayer(Interface):
    """
    """

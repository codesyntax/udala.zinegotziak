
from logging import getLogger
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


def vocab_term_title(context, name, termname):
    try:
        factory = getUtility(IVocabularyFactory, name)(context)
        termtitle = factory.getTerm(termname)
        return termtitle.title
    except:
        log = getLogger('vocab_term_title ERROR')
        log.info(f'Vocabulary: {name}, Term: {termname}')
        return ""
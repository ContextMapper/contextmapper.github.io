from pygments.lexer import RegexLexer, words, include, bygroups
from pygments.token import *
import re

class CMLLexer(RegexLexer):
    name = 'CML'
    aliases = ['cml']
    filenames = '*.cml'
    flags = re.MULTILINE | re.DOTALL

    tokens = {
       'comments': [
            (r'/\*.*?\*/', Comment),
            (r'//.*?\n', Comment),
        ],
       'strings': [
            (r'".*?"', String)
       ],
       'root': [
           include('comments'),
           include('strings'),
           (r'(BoundedContext)(\s*)([a-zA-z]*)(\s*)(implements)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Keyword, Text, Text)),
           (r'(BoundedContext)(\s*)([a-zA-z]*)(\s*)(realizes)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Keyword, Text, Text)),
           (r'(BoundedContext)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Aggregate)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Entity)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(ValueObject)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(DomainEvent)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Subdomain)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Module)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(PortCode)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(int)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(BigDecimal)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(String)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(contains)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(responsibilities)(\s*)(=)(\s*)([a-zA-z]*)(\s*)(,)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Text, Text, Text, Text, Text)),
           (r'(responsibilities)(\s*)(=)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(@[a-zA-Z_]*)(\s*)', bygroups(Text, Text)),
           (r'(-)(\s*)([a-zA-Z<>]*)(\s*)([a-zA-z]*)', bygroups(Text, Text, Keyword, Text, Text)),
           (r'([a-zA-z]*)(\s*)(<->)(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-z-]*)', bygroups(Text, Text, Text, Text, Text, Text, Text, Text, Keyword)),
           (r'([a-zA-z]*)(\s*)(->)(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-z-]*)', bygroups(Text, Text, Text, Text, Text, Text, Text, Text, Keyword)),
           (r'([a-zA-z]*)(\s*)(<-)(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-z-]*)', bygroups(Text, Text, Text, Text, Text, Text, Text, Text, Keyword)),
           (r'(upstream)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)(,)(\s*)([a-zA-Z_]*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword)),
           (r'(upstream)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text)),
           (r'(downstream)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)(,)(\s*)([a-zA-Z_]*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword)),
           (r'(downstream)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text)),
           (r'(supplier)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)(,)(\s*)([a-zA-Z_]*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword)),
           (r'(supplier)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text)),
           (r'(customer)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)(,)(\s*)([a-zA-Z_]*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword)),
           (r'(customer)(\s*)(implements)(\s*)([a-zA-Z_]*)(\s*)', bygroups(Keyword, Text, Keyword, Text, Keyword, Text)),
           (r'(ANTICORRUPTION_LAYER|APPLICATION|AS_IS|AccessObject|Aggregate|Application|ApplicationPart|Bag|BasicType|'
            r'BigDecimal|BigInteger|Blob|Boolean|BoundedContext|CHAR|CONCRETE|CONFORMIST|CORE_DOMAIN|Clob|Collection|'
            r'CommandEvent|Consumer|ContextMap|Customer-Supplier|DELETE|DataTransferObject|Date|DateTime|DomainEvent|'
            r'Double|Entity|FEATURE|Float|GENERIC_SUBDOMAIN|GET|INTEGER|Integer|JOINED|Key|List|Long|META|Module|None|'
            r'OPEN_HOST_SERVICE|ORGANIZATIONAL|Object\[\]|POST|PUBLISHED_LANGUAGE|PUT|PagedResult|PagingParameter|Partnership|'
            r'Repository|Resource|SINGLE_TABLE|STRING|SUPPORTING_DOMAIN|SYSTEM|SYSTEM_LANDSCAPE|Service|Set|Shared-Kernel|'
            r'String|Subdomain|TEAM|TO_BE|Timestamp|Trait|Upstream-Downstream|ValueObject|abstract|aggregateRoot|assertFalse|'
            r'assertTrue|auditable|basePackage|belongsTo|boolean|build|cache|cascade|changeable|condition|construct|contains|'
            r'creditCardNumber|customer|databaseColumn|databaseJoinColumn|databaseJoinTable|databaseTable|databaseType|decimalMax|'
            r'decimalMin|digits|discriminatorColumn|discriminatorLength|discriminatorType|discriminatorValue|domainVisionStatement|'
            r'double|downstream|email|enum|eventBus|extends|external|fetch|float|future|gap|groupBy|hint|immutable|'
            r'implementationTechnology|implements|import|index|inheritanceType|inject|int|inverse|key|knowledgeLevel|'
            r'length|long|map|max|min|nogap|notBlank|notEmpty|nullable|optimisticLocking|orderBy|orderColumn|orderby|'
            r'ordinal|package|past|path|pattern|persistent|private|protected|public|publish|query|queueName|range|realizes|'
            r'required|responsibilities|return|scaffold|scriptAssert|select|size|state|subscribe|supplier|throws|to|topicName|'
            r'transient|type|upstream|url|valid|validate|webservice|'
            r'with)\b', Keyword),
           ('\s+', Text),
           ('\{|\=|\}|\-|:', Text),
       ]
   }

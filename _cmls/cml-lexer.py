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
           (r'(ContextMap)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(BoundedContext)(\s*)([a-zA-z]*)(\s*)(implements)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Keyword, Text, Text)),
           (r'(BoundedContext)(\s*)([a-zA-z]*)(\s*)(refines)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Keyword, Text, Text)),
           (r'(BoundedContext)(\s*)([a-zA-z]*)(\s*)(realizes)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Keyword, Text, Text)),
           (r'(BoundedContext)(\s*)([a-zA-z0-9]*)', bygroups(Keyword, Text, Text)),
           (r'(UseCase)(\s*)([a-zA-z0-9]*)', bygroups(Keyword, Text, Text)),
           (r'(UserStory)(\s*)([a-zA-z0-9]*)', bygroups(Keyword, Text, Text)),
           (r'(Aggregate)(\s*)([a-zA-z0-9]*)', bygroups(Keyword, Text, Text)),
           (r'(Entity)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(ValueObject)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(DomainEvent)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(DomainObject)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Domain)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Subdomain)(\s*)([a-zA-z]*)(\s*)(supports)(\s*)([a-zA-z]*)(\s*)(,)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Keyword, Text, Text, Text, Text, Text, Text)),
           (r'(Subdomain)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Module)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(UnknownType)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text)),
           (r'(BigDecimal)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(String)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(basePackage)(\s*)(=)(\s*)([a-z\.]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(TrackingId)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Repository)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Service)(\s+)([a-zA-Z0-9_]*)', bygroups(Keyword, Text, Text)),
           (r'(boolean)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(def)(\s*)(List)(<)([a-zA-Z@]*)(>)(\s*)([a-zA-Z]*)(\()(List)(<)([a-zA-Z@]*)(>)(\s*)([a-zA-Z0-9]*)(\))([;])', bygroups(Keyword, Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'(List)(<)(String)(>)(\s*)([a-zA-Z]*)', bygroups(Keyword, Text, Keyword, Text, Text, Text)),
           (r'(List)(<[@a-zA-Z]*>)(\s*)([a-zA-Z]*)', bygroups(Keyword, Text, Text, Text)),
           (r'(-)(\s*)(List)(<[@a-zA-Z]*>)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text, Text)),
           (r'(@Cargo)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Text)),
           (r'(contains)(\s*)([a-zA-Z0-9_, ]*)', bygroups(Keyword, Text, Text)),
           (r'(throws)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(def)(\s*)([a-zA-z0-9@\s\(\),]*)([;])', bygroups(Keyword, Text, Text, Text)),
           (r'(store)', bygroups(Text)),
           (r'(find)', bygroups(Text)),
           (r'(unLocode)', bygroups(Text)),
           (r'(routeSpecification)', bygroups(Text)),
           (r'(lookupHandlingHistoryOfCargo)', bygroups(Text)),
           (r'(Type)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(PortCode)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(Date)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(PaymentStatus)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(HandlingEvent.Type)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(ItineraryNumber)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(enum)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(responsibilities)(\s*)(=)(\s*)([a-zA-z, ]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(owner)(\s*)(=)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(owner)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(likelihoodForChange)(\s*)(=)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(useCases)(\s*)(=)(\s*)([a-zA-z, 0-9]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(userStories)(\s*)(=)(\s*)([a-zA-z, 0-9]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(features)(\s*)(=)(\s*)([a-zA-z, 0-9]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(reads)(\s*)([a-zA-z, ]*)', bygroups(Keyword, Text, Text)),
           (r'(writes)(\s*)([a-zA-z, ]*)', bygroups(Keyword, Text, Text)),
           (r'(actor)(\s*)(=)(\s*)([a-z\.]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(actor)(\s*)(\s*)([a-z\.]*)', bygroups(Keyword, Text, Text, Text)),
           (r'(level)(\s*)(=)(\s*)([a-z\.]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(level)(\s*)(\s*)([a-z\.]*)', bygroups(Keyword, Text, Text, Text)),
           (r'(scope)(\s*)(=)(\s*)([a-z\.]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(scope)(\s*)(\s*)([a-z\.]*)', bygroups(Keyword, Text, Text, Text)),
           (r'(interactions)(\s*)(=)(\s*)', bygroups(Keyword, Text, Text, Text)),
           (r'(interactions)(\s*)(\s*)', bygroups(Keyword, Text, Text)),
           (r'(benefit)(\s*)(=)(\s*)([a-zA-Z\.]*)', bygroups(Keyword, Text, Text, Text, Text)),
           (r'(benefit)(\s*)(\s*)([a-zA-Z\.]*)', bygroups(Keyword, Text, Text, Text)),
           (r'(exposedAggregates)(\s*)(=)(\s*)([a-zA-z0-9]*)(\s*)(,)(\s*)([a-zA-z0-9]*)', bygroups(Keyword, Text, Text, Text, Text, Text, Text, Text, Text)),
           (r'(exposedAggregates)(\s*)(=)(\s*)([a-zA-z]*)(\s*)', bygroups(Keyword, Text, Text, Text, Text, Text)),
           (r'(exposedAggregates)(\s*)([a-zA-z0-9]*)(\s*)(,)(\s*)([a-zA-z0-9]*)', bygroups(Keyword, Text, Text, Text, Text, Text, Text)),
           (r'(exposedAggregates)(\s*)([a-zA-z]*)(\s*)', bygroups(Keyword, Text, Text, Text)),
           (r'(downstreamRights)(\s*)(=)(\s*)([A-Z_]*)(\s*)', bygroups(Keyword, Text, Text, Text, Text, Text)),
           (r'(downstreamRights)(\s*)([A-Z_]*)(\s*)', bygroups(Keyword, Text, Text, Text)),
           (r'(int)(\s*)([a-zA-z]*)', bygroups(Keyword, Text, Text)),
           (r'(-)(\s*)([a-zA-Z<>]*)(\s*)([a-zA-z]*)', bygroups(Text, Text, Keyword, Text, Text)),

           (r'([a-zA-z]*)(\s*)(\[)(P)(\])(<->)(\[)(P)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'(\[)(P)(\])([a-zA-z]*)(\s*)(<->)(\s*)(\[)(P)(\])([a-zA-z]*)', bygroups(Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-z]*)(\[)(P)(\])(\s*)(<->)(\s*)([a-zA-z]*)(\[)(P)(\])', bygroups(Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text)),
           (r'(\[)(P)(\])([a-zA-z]*)(\s*)(<->)(\s*)([a-zA-z]*)(\[)(P)(\])', bygroups(Text, Keyword, Text, Text, Text, Text, Text, Text, Text, Keyword, Text)),

           (r'([a-zA-z]*)(\s*)(\[)(SK)(\])(<->)(\[)(SK)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-z-]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)(SK)(\])(<->)(\[)(SK)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'(\[)(SK)(\])([a-zA-z]*)(\s*)(<->)(\s*)(\[)(SK)(\])([a-zA-z]*)', bygroups(Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-z]*)(\[)(SK)(\])(\s*)(<->)(\s*)([a-zA-z]*)(\[)(SK)(\])', bygroups(Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text)),
           (r'(\[)(SK)(\])([a-zA-z]*)(\s*)(<->)(\s*)([a-zA-z]*)(\[)(SK)(\])', bygroups(Text, Keyword, Text, Text, Text, Text, Text, Text, Text, Keyword, Text)),
           (r'([a-zA-z]*)(\s*)(<->)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Text, Text)),

           (r'([a-zA-z]*)(\s*)(<->)(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-z-]*)', bygroups(Text, Text, Text, Text, Text, Text, Text, Text, Keyword)),
           (r'([a-zA-z]*)(\s*)(\[)(SK)(\])(<->)(\[)(SK)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)(P)(\])(<->)(\[)(P)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-z-]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(<-)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(<-)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-Z_]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text)),

           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(->)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-Z_]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(->)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text)),

           (r'([a-zA-z]*)(\s*)(<-)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(<-)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(<-)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(<-)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text)),

           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(->)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(->)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(->)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(->)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])(->)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(->)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(->)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Keyword, Text, Keyword,  Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(,)([A-Z]*)(\])(->)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Keyword, Text, Keyword, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(->)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)(\s*)(:)(\s*)([a-zA-Z_])', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(->)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'(\[)([A-Z]*)(\])([a-zA-z]*)(\s*)(->)(\s*)(\[)([A-Z]*)(\])([a-zA-z]*)', bygroups(Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-z]*)(\[)([A-Z]*)(\])(\s*)(->)(\s*)([a-zA-z]*)(\[)([A-Z]*)(\])', bygroups(Text, Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text)),
           (r'(\[)([A-Z]*)(\])([a-zA-z]*)(\s*)(->)(\s*)([a-zA-z]*)(\[)([A-Z]*)(\])', bygroups(Text, Keyword, Text, Text, Text, Text, Text, Text, Text, Keyword, Text)),
           (r'([a-zA-z]*)(\s*)(\[)([A-Z]*)(\])(->)(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Keyword, Text, Text, Text, Text)),
           (r'([a-zA-z]*)(\s*)(->)(\[)([A-Z]*)(\])(\s*)([a-zA-z]*)', bygroups(Text, Text, Text, Text, Keyword, Text, Text, Text)),
           (r'([a-zA-Z0-9]*)(\s*)(->)(\s*)([a-zA-Z0-9]*)', bygroups(Text, Text, Text, Text, Text)),
           (r'([a-zA-Z]*)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)(Upstream-Downstream)(\s*)(\[)([A-Z]*)(\])([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Keyword, Text, Text, Keyword, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\[)([A-Z]*)(,)([A-Z]*)(\])(\s*)(Upstream-Downstream)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Keyword, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\[)([A-Z]*)(\])(\s*)(Downstream-Upstream)(\s*)(\[)([A-Z]*)(,)([A-Z]*)(\])([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text, Keyword, Text, Text, Keyword, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\[)([A-Z]*)(\])(\s*)(Downstream-Upstream)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\s*)(Upstream-Downstream)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\s*)(Downstream-Upstream)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\s*)(Partnership)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\[)([A-Z]*)(\])(\s*)(Customer-Supplier)(\s*)(\[)([A-Z]*)(\])([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text, Keyword, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\[)([A-Z]*)(\])(\s*)(Supplier-Customer)(\s*)(\[)([A-Z]*)(\])([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text, Keyword, Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\s*)(Customer-Supplier)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\s*)(Supplier-Customer)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text)),
           (r'([a-zA-Z]*)(\s*)(Shared-Kernel)(\s*)([a-zA-Z]*)(\s*)(:)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text, Text, Text, Text, Text)),
           (r'([a-zA-Z]*)(\s*)(Shared-Kernel)(\s*)([a-zA-Z]*)', bygroups(Text, Text, Keyword, Text, Text)),

           (r'(\[)(U)(,)(S)(\])([a-zA-Z]*)(\s*)(->)(\s*)(\[)(D)(,)(C)(\])([a-zA-Z]*)', bygroups(Text, Keyword, Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text, Keyword, Text, Text)),
           (r'(\[)(U)(,)(S)(\])([a-zA-Z]*)(\s*)(->)(\s*)([a-zA-Z]*)(\[)(D)(,)(C)(\])', bygroups(Text, Keyword, Text, Keyword, Text, Text, Text, Text, Text, Text, Text, Keyword, Text, Keyword, Text)),
           (r'([a-zA-Z]*)(\[)(U)(,)(S)(\])(\s*)(->)(\s*)([a-zA-Z]*)(\[)(D)(,)(C)(\])', bygroups(Text, Text, Keyword, Text, Keyword, Text, Text, Text, Text, Text, Text, Keyword, Text, Keyword, Text)),

           (r'(realizes)(\s*)([a-zA-Z]*)', bygroups(Keyword, Text, Text)),
           (r'(isLatencyCritical)(\s*)(=)(\s*)(true)', bygroups(Keyword, Text, Text, Text, Text)),
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
            r'transient|type|upstream|url|valid|validate|webservice|NOT_RECEIVED|IN_PORT|ONBOARD_CARRIER|CLAIMED|UNKNOWN|a|an|As|I|want|to|so|that|create|update|delete|read|'
            r'with|its|for|NOT_ROUTED|ROUTED|MISROUTED|downstreamRights|INFLUENCER|OPINION_LEADER|VETO_RIGHT|DECISION_MAKER|MONOPOLIST|securityZone|securityAccessGroup|structuralVolatility|OFTEN|NORMAL|RARELY|contentVolatility|LOW|HIGH|availabilityCriticality|consistencyCriticality|TINY|HUGE|storageSimilarity|securityCriticality|aggregateLifecycle|write|read-only|X)\b', Keyword),
           ('\s+', Text),
           (r'([a-zA-Z0-9]*)(;)', bygroups(Text, Text)),
           (r'([a-zA-Z0-9@]*)(\s*)([a-zA-Z0-9]*)(\s*)(\()([a-zA-Z0-9]*)(\s*)([a-zA-Z0-9]*)(\))(;)', bygroups(Text, Text, Text, Text, Text, Text, Text, Text, Text, Text)),
           (r'([@a-zA-Z0-9]+)', bygroups(Text)),
           ('\{|\=|\}|\-|:|;|,|\(|\)|\[|\]|\_', Text),
       ]
   }

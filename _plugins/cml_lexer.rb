# frozen_string_literal: true

# Rouge lexer for the Context Mapper DSL (CML), used for ```cml code blocks.
# The keywords are taken from the Xtext grammars of the DSL (ContextMappingDSL.xtext and TacticDDDLanguage.xtext);
# like the editor, it highlights them wherever they appear outside of strings and comments.

require 'rouge'
require 'set'

module Rouge
  module Lexers
    class CML < RegexLexer
      title 'CML'
      desc 'Context Mapper DSL (https://contextmapper.org)'
      tag 'cml'
      filenames '*.cml'

      KEYWORDS = Set.new(%w(
      ACT APPLICATION AS_IS AUTONOMY AccessObject Aggregate Application ApplicationPart
      BasicType BoundedContext CARE CHAR COMMODITY CONCRETE CONTROL CORE_DOMAIN CUSTOM_BUILT
      Command CommandEvent Consumer ContextMap Coordination Customer-Supplier DECISION_MAKER
      DELETE DataTransferObject Domain DomainEvent Downstream-Upstream Entity Event FAIRNESS
      FEATURE Flow GENERIC_SUBDOMAIN GENESIS GET HIGH HUGE INCLUSIVENESS INFLUENCER INNOVATION
      INTEGER Invariant JOINED LOW MEDIUM META MONITOR MONOPOLIST Module NORMAL None O OFTEN
      OPINION_LEADER ORGANIZATIONAL PERFECTION POST PRIVACY PRODUCT PUT Partnership RARELY
      RESPECT Repository Resource SINGLE_TABLE STRING SUPPORTING_DOMAIN SUSTAINABILITY SYSTEM
      SYSTEM_LANDSCAPE Service Shared-Kernel Stakeholder StakeholderGroup Stakeholders Subdomain
      Supplier-Customer TEAM TINY TO_BE TRANSPARENCY TRUST TacticDDDApplication Trait UNDEFINED
      Upstream-Downstream UseCase UserStory VETO_RIGHT Value ValueCluster ValueEpic
      ValueNarrative ValueObject ValueRegister ValueWeigthing X a abstract action actor
      aggregateLifecycle aggregateRoot an are assertFalse assertTrue association auditable
      availabilityCriticality bad basePackage belongsTo benefit build businessModel cache
      cascade changeable command condition consequences consistencyCriticality construct
      contains contentVolatility core create creditCardNumber databaseColumn databaseJoinColumn
      databaseJoinTable databaseTable databaseType decimalMax decimalMin def delete demonstrator
      description digits discriminatorColumn discriminatorLength discriminatorType
      discriminatorValue domainVisionStatement downstreamRights email enum event eventBus
      evolution exposedAggregates extends external features fetch for future gap good groupBy
      harmed hint immutable impact implementationTechnology implements import in index influence
      inheritanceType inject interactions interest inverse is isCore key knowledgeLevel length
      level likelihoodForChange map max min neutral nogap nonResponsibilities not notBlank
      notEmpty nullable o of operation opposingValue opposite optimisticLocking orderBy
      orderColumn orderby ordinal owner package past path pattern persistent priority private
      promoted protected public publish query queueName range read read-only realizes reduced
      reference refines relatedValue required responsibilities return scaffold scope
      scriptAssert secondaryActors securityAccessGroup securityCriticality securityZone select
      size stakeholder state storageSimilarity structuralVolatility subscribe supports the
      throws to topicName transient triggers type unique update url useCases userRequirements
      userStories valid validate values webservice with write x
      )).freeze

      # relationship roles and patterns in Context Maps ([U,OHS,PL] -> [D,ACL])
      ROLES = Set.new(%w(ACL C CF D OHS P PL S SK U)).freeze

      TYPES = Set.new(%w(
      Bag BigDecimal BigInteger Blob Boolean Clob Collection Date DateTime Double Float Integer
      Key List Long Map Object PagedResult PagingParameter Set String Timestamp boolean double
      float int long void
      )).freeze

      # keywords that consist of several words (longest first)
      PHRASES = [
        'with the following externally observable and/or internally auditable behavior:',
        'stakeholders expect it to promote, protect or create',
        'possibly degrading or prohibiting',
        'running the risk of harms such as',
        'In the context of the SOI,',
        'expecting benefits such as',
        'When the SOI executes',
        'as demonstrated in',
        'accepting that',
        'realization of',
        'unmarshall to',
        'delegates to',
        'initiated by',
        'reduction of',
        'emits event',
        'with their',
        'I want to',
        'more than',
        'and that',
        'split by',
        'with its',
        'I value',
        'so that',
        'As an',
        'As a'
      ].freeze

      PHRASE_REGEX = Regexp.new('\\b(?:' + PHRASES.map { |p| Regexp.escape(p).gsub('\\ ') { '\\s+' } }.join('|') + ')(?!\\w)')


      state :root do
        rule %r/\s+/, Text
        rule %r(//.*?$), Comment::Single
        rule %r(/\*.*?\*/)m, Comment::Multiline
        rule %r/"(?:\\.|[^"\\])*"/, Str::Double
        rule %r/'(?:\\.|[^'\\])*'/, Str::Single
        rule PHRASE_REGEX, Keyword
        rule %r/[A-Za-z_]\w*(?:-[A-Za-z_]\w*)*/ do |m|
          word = m[0]
          if KEYWORDS.include?(word)
            token Keyword
          elsif ROLES.include?(word)
            token Name::Class
          elsif TYPES.include?(word)
            token Keyword::Type
          else
            token Name
          end
        end
        rule %r/\d+(?:\.\d+)?/, Num
        rule %r/<->|->|<-|=>|::|[\[\]{}(),;:=*+!<>@.\/-]/, Punctuation
        rule %r/./, Text
      end
    end
  end
end

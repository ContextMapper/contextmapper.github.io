# frozen_string_literal: true

# Rouge lexer for the Microservice Domain-Specific Language (MDSL, https://microservice-api-patterns.github.io/MDSL-Specification/),
# used for ```mdsl code blocks. The keywords are taken from the Xtext grammar of MDSL (APIDescription.xtext).

require 'rouge'
require 'set'

module Rouge
  module Lexers
    class MDSL < RegexLexer
      title 'MDSL'
      desc 'Microservice Domain-Specific Language (https://microservice-api-patterns.github.io/MDSL-Specification/)'
      tag 'mdsl'
      filenames '*.mdsl'

      KEYWORDS = Set.new(%w(
      AGGRESSIVE_OBSOLESCENCE AMQP APACHE_CAMEL_ROUTE API API_CALL_SEQUENCING API_KEY API_Key
      API_MOCK APPLICATION_FLOW AT_LEAST_ONCE AT_MOST_ONCE AVRO_SCHEMA Aggregated_Metadata
      Annotated_Parameter_Collection Avro_RPC BACKEND_INTEGRATION BACKEND_INTEGRATION_SCENARIO
      BASIC_AUTHENTICATION BODY BPEL_PROCESS BPMN_PROCESS BUSINESS_ACTIVITY_PROCESSOR
      BUSINESS_API COLLECTION_RESOURCE COMMAND_MESSAGE COMMUNITY_API COMPETEING_CONSUMER
      COMPUTATION_FUNCTION COOKIE CORRELATION_ID CQRS CRUD CRUDSF Command Command_Message
      Context_Representation Control_Metadata DATA_QUOTA DATA_TRANSFER_RESOURCE DATA_TYPE
      DEAD_LETTER DELETE DOCUMENT_MESSAGE DURABLE_SUBSCRIBER Data Data_Element Document_Message
      ETERNAL_LIFETIME EVENT_DRIVEN_CONSUMER EVENT_MESSAGE EVENT_PROCESSOR EVENT_SOURCING
      EXACTLY_ONCE EXPERIMENTAL_PREVIEW Embedded_Entity Error_Report Event_Message FREEMIUM
      FRONTEND_INTEGRATION FRONTEND_INTEGRATION_SCENARIO GB GET GRAPHQL_SDL GUARANTEED_DELIVERY
      HEAD HEADER HTTP IDEMPOTENT_RECEIVER IMPLICIT INFORMAL INFORMATION_HOLDER_RESOURCE
      INTEGRATION_FLOW INVALID_MESSAGE IPA Id_Element Identifier Identifier_Element JMS_ActiveMQ
      JOB_STORY JOLIE_TYPE JSON-RPC JSON_SCHEMA JWT Java Kafka LIMITED_GUARANTEED_LIFETIME
      LINK_LOOKUP_RESOURCE Link Link_Element Linked_Information_Holder MAP_TYPE
      MASTER_DATA_HOLDER MAX_CALLS MB MESSAGE_DISPATCHER MESSAGE_EXPIRES MESSAGING_GATEWAY
      MESSAGING_MAPPER MQTT MUTABLE_COLLECTION_RESOURCE Metadata Metadata_Element NONE
      NOTIFICATION O OAUTH_FLOW OAUTH_IMPLICIT ONE_WAY OPERATIONAL_DATA_HOLDER OPTIONS OTHER
      OTHER_STRATEGY PATCH PATH PLAIN_PROGRAMMING POINT_TO_POINT POLLING_CONSUMER POST
      PROCESSING_RESOURCE PROTOCOL_BUFFER PUBLIC_API PUBLISH_SUBSCRIBE PUT Pagination PlainJava
      Provenance_Metadata QUALITATIVE QUANTITATIVE QUERY REFERENCE_DATA_HOLDER REQUEST_REPLY
      RETRIEVAL_OPERATION Request_Bundle Request_Condition Response_Bundle SELECTIVE_CONSUMER
      SEQUENCE_ID SERVICE_ACTIVATOR SERVICE_ORCHESTRATION SLA SOAP_HTTP SOLUTION_INTERNAL_API
      SPRING_INTEGRATION_FLOW STATEFUL_PROCESSING_RESOURCE STATELESS_PROCESSING_RESOURCE
      STATE_CREATION_OPERATION STATE_DELETION_OPERATION STATE_REPLACEMENT_OPERATION
      STATE_TRANSITION_OPERATION STOMP STRING SUBSCRIPTION String TEST_CASE THRIFT_TYPE TRACE
      TRANSACTIONAL_CLIENT TRANSFORMATION_RESOURCE TWO_IN_PRODUCTION Thrift UNDISCLOSED UNKNOWN
      USAGE_BASED USER_STORY VALIDATION_RESOURCE Version_Identifier Web_Sockets Wish_List
      Wish_Template X XML_SCHEMA YET_ANOTHER_FLOW_LANGUAGE a accepts action against all
      alternative alternatively an analytics and any are as at bidirectional binding bindings
      broker by channel channels client command commands compensated conditions consumed
      consumes context conversation data default delivering delivery description durable dynamic
      element elements emit emits emitting endpoint error event events evolution expecting
      exposes extending external false flow follows for from gRPC gateway governance guarantee
      headers hours if implementation implemented in initiated input into is its limit links
      location m media mediates mediation message minimal minutes notification o objective of
      offers on operation optimal or overview package parallel parameter parameters path payload
      penalty plan policy produces protected protocol provider rate realized realizes receives
      relation replies reply report reporting request resource responsibility role s scenario
      seconds server serves so static status story stream structured subscriptions supports
      target targets template that the through to transitions trigger triggers true type under
      usage uses using version via wants when where with within x xor yielding
      )).freeze

      # element roles in data types ("name":D<string>, P for unspecified parameters)
      ROLES = Set.new(%w(D ID L MD P)).freeze

      TYPES = Set.new(%w(bool boolean byte char double float int long raw short string void)).freeze

      state :root do
        rule %r/\s+/, Text
        rule %r(//.*?$), Comment::Single
        rule %r(/\*.*?\*/)m, Comment::Multiline
        rule %r/"(?:\\.|[^"\\])*"/, Str::Double
        rule %r/'(?:\\.|[^'\\])*'/, Str::Single
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
        rule %r/\d+(?:\.\d+)*/, Num
        rule %r/<<|>>|<=|>=|==|!=|[\[\]{}()<>,;:=*+?!|.\/-]/, Punctuation
        rule %r/./, Text
      end
    end
  end
end

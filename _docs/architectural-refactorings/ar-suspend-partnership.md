---
title: "AR-9: Suspend Partnership"
permalink: /docs/ar-suspend-partnership/
---

Provides different approaches to suspend a Partnership relationship.

## Context & Rationales
The Partnership pattern describes a close relationship where two development teams are interdependent. For some reason they can
only succeed or fail together. New developments and releases must be coordinated between the teams. However, this requires a lot
of coordination and communication between the teams and in some situations it might be beneficial to suspend such a partnership 
in order to increase team autonomy.

## Goal
This AR provides three strategies to suspend a Partnership relationship. Each strategy fulfills the goal to remove the partnership
relationship and replace it with another strategy how the two Bounded Contexts depend on each other. The strategies are:

 * **a) Merge the two Bounded Contexts:**
   
   Since the two teams have to work very closely together, a solution might be to merge the teams and see them as one single Bounded Context.
   This strategy basically calls the [AR-7 Merge Bounded Contexts](./../AR-7-Merge-Bounded-Contexts) refactoring to merge the two contexts.

   <div class="alert alert-custom">
   <strong>Known limitation:</strong> Unfortunately, this strategy does not work in <a href="/docs/vs-code/">VS Code</a> and <a href="/docs/online-ide/">online</a> in case the removed Bounded Context is referenced in a Context Map. This is due to <a href="https://github.com/eclipse/xtext-core/issues/1494">a bug in the Xtext framework</a>.
   </div>

   
 * **b) Extract a new Bounded Context for commonalities and establish upstream-downstream relationships:**
 
   The interdependence may come from common parts within the domain model or APIs which are maintained by both teams. In such a case it might 
   be a solution to extract common parts to a new Bounded Context. A new team may maintain these parts an offer corresponding APIs which
   can be used by the existing Bounded Contexts. This strategy extracts a new Bounded Context and creates two upstream-downstream
   relationships between the new and the two existing Bounded Contexts.
   
 * **c) Simply replace the Partnership with an upstream-downstream relationship:**
 
   Another solution might be that one of the two teams takes the lead regarding common parts or APIs. Decisions regarding changes on these
   common parts are only done by this leading team. All parts which both contexts depend on are moved to the leading context. Thus, the
   dependency becomes unidirectional. This strategy replaces the Partnership relationship with an upstream-downstream relationship. If you
   select this strategy you have to define which Bounded Context becomes the upstream context. 

## Preconditions
 * Your model needs **at least two bounded contexts** which are in a **Partnership** relationship.

## Input
 * The Partnership relationship.
 
## Output
The output of this AR depends on the selected mode:
  * a) One (merged) bounded context containing all aggregates of the two input bounded contexts.
  * b) A new Bounded Context for commonalities and two new upstream-downstream relationships between the new and the two existing Bounded Context.
  * c) The same model but the Partnership relationship will be replaced with an upstream-downstream relationship.
 
## Example
The following example illustrates how this AR can be applied. The corresponding sources can be found in our 
[examples repository](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings).

### Input
The following model contains a Partnership relationship. Therefore the AR is available with a right-click on the relationship (arrow):

<a href="/img/suspend-partnership-input.png">![Suspend Partnership Example Input](/img/suspend-partnership-input.png)</a>

### Results
The result of applying this AR depends on the selected strategy to suspend the relationship. The following dialog asks the user which
strategy shall be applied:

<a href="/img/suspend-partnership-mode-selection-dialog.png">![Suspend Partnership Mode Selection Dialog](/img/suspend-partnership-mode-selection-dialog.png)</a> 

#### Result for "Merge the two Bounded Contexts"
If you choose to merge the two Bounded Contexts, a second page in the wizard allows you to specify whether the attributes which cannot
be merged shall be taken from the second Bounded Context or not (see [AR-7: Merge Bounded Contexts](/docs/ar-merge-bounded-contexts/)
for details):

<a href="/img/suspend-partnership-merge-page.png">![Suspend Partnership Merge Mode Page](/img/suspend-partnership-merge-page.png)</a>

The resulting model contains the merged Bounded Context containing all Aggregates of the two original Bounded Contexts:

<a href="/img/suspend-partnership-output-a.png">![Suspend Partnership Example Output for 'MERGE' Strategy](/img/suspend-partnership-output-a.png)</a>

#### Result for "Extract a new Bounded Context for commonalities and establish upstream-downstream relationships"
If the user chooses to extract a new Bounded Context, the result will contain the new context for commonalities and two additional 
upstream-downstream relationships between the new and the existing Bounded Contexts:

<a href="/img/suspend-partnership-output-b.png">![Suspend Partnership Example Output for 'EXTRACT' Strategy](/img/suspend-partnership-output-b.png)</a>

#### Result for "Simply replace the Partnership with an upstream-downstream relationship"
The last strategy removes the existing Partnership relationship from the model and replaces it with a new upstream-downstream relationship.
In this case, the user has to select which Bounded Context becomes the upstream:

<a href="/img/suspend-partnership-upstream-selection.png">![Suspend Partnership 'REPLACE' Mode Upstream Selection](/img/suspend-partnership-upstream-selection.png)</a>

With the selection above, the AR produces the following result:

<a href="/img/suspend-partnership-output-c.png">![Suspend Partnership Example Output for 'REPLACE' Strategy](/img/suspend-partnership-output-c.png)</a>

## Example Sources
 * You can find the CML sources for this AR example 
   [here](https://github.com/ContextMapper/context-mapper-examples/tree/master/src/main/cml/architectural-refactorings/AR-9-Suspend-Partnership).

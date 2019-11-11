---
title: "AR-11: Change Partnership to Shared Kernel"
permalink: /docs/ar-change-partnership-to-shared-kernel/
---

This simple relationship refactoring changes a Partnership relationship on a Context Map to a Shared Kernel relationship.

## Summary
Our relationship refactorings allow the user/modeller to change the type of a relationship on a Context Map easily without manual work.
The symmetric relationships according to our [semantic model](/docs/language-model/), Shared Kernel and Partnership, are interchangeable without impacts
to the structure of the decomposition. This refactoring changes a Partnership relationship to a Shared Kernel relationship.

## Example
The following small example illustrates how this refactoring can be applied. With a right-click on a Partnership relationship, you can apply
_Change to Shared Kernel_:

<a href="/img/change-partnership-to-shared-kernel-input.png">![Change Partnership to Shared Kernel Example Input](/img/change-partnership-to-shared-kernel-input.png)</a>

The refactoring will simply change the relationship to a Shared Kernel relationship:
<a href="/img/change-partnership-to-shared-kernel-output.png">![Change Partnership to Shared Kernel Example Output](/img/change-partnership-to-shared-kernel-output.png)</a>

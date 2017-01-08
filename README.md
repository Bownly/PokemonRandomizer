# Pokemon Randomizers

Contained in this repository are scripts for randomizing the pokemon distribution for various pokemon games. All of them follow the same general design principles:
- Pokemon are swapped by families of equal size. Meaning that you could have a build where the Caterpie line is replaced with the Abra line, since both families contain 3 sequential species. You would never end up with a scenario where the Caterpie line is replaced with, say, the Spearow line, since the two families are of sizes 3 and 2 respectively.
- Swaps are not necessarily reciprocal. Meaning that, using the previous example where the Caterpie line is replaced with the Abra line, it's not likely that the Abra line is replaced with the Caterpie line. It's possible, but unlikely. (In fact, it's possible for any pokemon family to be replaced by itself!)
- Swaps are global. Again, let's go with the Caterpie -> Abra example. Every place that a Caterpie would normally be catchable, instead, you'd encounter an Abra. Same for Metapod and Kadabra, and Butterfree and Alakazam. These scripts don't edit the teams of other trainers or anything like that. Just wild pokemon and in some cases, starter/gift/fossil/etc pokemon.


# How to run
You pretty much just run the script and then build the ROMs as normal. But note that you'll need to provide your own copy of the disassembly of the respective game. (See the respective readme files in each folder for any specifics.)


# Possible future features

- Adapt the script for GSC/Brown/etc
- Have the code output an ips instead of requiring the users to build their own ROM




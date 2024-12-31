import random
import time
from colorama import init, Fore

init(autoreset=True)


code_lines_group1 = [
    "struct group_info init_groups = { .usage = ATOMIC_INIT(2) };",
    "",
    "struct group_info *groups_alloc(int gidsetsize){",
    "",
    "    struct group_info *group_info;",
    "    int nblocks;",
    "    int i;",
    "",
    "    nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;",
    "    nblocks = nblocks ? : 1;",
    "    group_info = kmalloc(sizeof(*group_info) + nblocks * sizeof(gid_t *), GFP_USER);",
    "    if (!group_info)",
    "        return NULL;",
    "",
    "    group_info->ngroups = gidsetsize;",
    "    group_info->nblocks = nblocks;",
    "    atomic_set(&group_info->usage, 1);",
    "",
    "    if (gidsetsize <= NGROUPS_SMALL)",
    "        group_info->blocks[0] = group_info->small_block;",
    "    else {",
    "        for (i = 0; i < nblocks; i++) {",
    "            gid_t *b;",
    "            b = (void *)__get_free_page(GFP_USER);",
    "            if (!b)",
    "                goto out_undo_partial_alloc;",
    "            group_info->blocks[i] = b;",
    "        }",
    "    }",
    "",
    "    return group_info;",
    "",
    "out_undo_partial_alloc:",
    "    while (--i >= 0) {",
    "        free_page((unsigned long)group_info->blocks[i]);",
    "    }",
    "    kfree(group_info);",
    "    return NULL;",
    "}"
]

code_lines_group2 = [
    "void process_group(struct group_info *group){",
    "    int i;",
    "",
    "    for (i = 0; i < group->ngroups; i++) {",
    "        gid_t *g = group->blocks[i];",
    "        if (!g)",
    "            break;",
    "        printf(\"Processing group ID: %d\\n\", g[i]);",
    "    }",
    "",
    "    if (i == group->ngroups)",
    "        printf(\"All groups processed successfully.\\n\");",
    "    else",
    "        printf(\"Error in processing group at index: %d\\n\", i);",
    "}"
]

code_lines_group3 = [
    "int init_user_session(char *username, int session_id){",
    "",
    "    if (session_id < 0 || username == NULL) {",
    "        printf(\"Invalid session parameters.\\n\");",
    "        return -1;",
    "    }",
    "",
    "    struct session_info *session;",
    "    session = kmalloc(sizeof(struct session_info), GFP_KERNEL);",
    "",
    "    if (!session) {",
    "        printf(\"Memory allocation failed for session.\\n\");",
    "        return -1;",
    "    }",
    "",
    "    strncpy(session->username, username, MAX_USERNAME_LEN);",
    "    session->session_id = session_id;",
    "    session->status = SESSION_ACTIVE;",
    "",
    "    printf(\"Session initialized for user: %s\\n\", username);",
    "    return 0;",
    "}"
]

code_lines_group4 = [
    "void terminate_session(struct session_info *session){",
    "",
    "    if (!session) {",
    "        printf(\"No active session to terminate.\\n\");",
    "        return;",
    "    }",
    "",
    "    if (session->status == SESSION_ACTIVE) {",
    "        session->status = SESSION_TERMINATED;",
    "        printf(\"Session terminated for user: %s\\n\", session->username);",
    "    } else {",
    "        printf(\"Session already terminated.\\n\");",
    "    }",
    "",
    "    kfree(session);",
    "}"
]

code_lines_group5 = [
    "void audit_user_activity(struct session_info *session){",
    "    if (!session || session->status != SESSION_ACTIVE) {",
    "        printf(\"No active session to audit.\\n\");",
    "        return;",
    "    }",
    "",
    "    printf(\"Auditing user: %s\\n\", session->username);",
    "",
    "    if (session->activity_count > 100) {",
    "        printf(\"User activity exceeds limit! Terminating session...\\n\");",
    "        terminate_session(session);",
    "    } else {",
    "        printf(\"User activity is within acceptable limits.\\n\");",
    "    }",
    "}"
]

all_code_groups = [code_lines_group1, code_lines_group2, code_lines_group3, code_lines_group4, code_lines_group5]

fun_facts = [
    "Fact: The first computer worm was called 'Creeper' and was written in 1971.",
    "Fact: In 2013, Adobe was hacked, exposing over 150 million user credentials.",
    "Fact: Only 5% of company folders are properly protected from cyber threats.",
    "Fact: Social engineering attacks account for 33% of all cyber attacks.",
    "Fact: The word 'phishing' was coined in the mid-1990s.",
    "Fact: The first antivirus software was created in 1987 by Bernd Fix to remove a virus called 'Vienna.'",
    "Fact: In 2000, the 'ILOVEYOU' worm spread through email and infected over 10 million computers in just a few hours.",
    "Fact: The longest-running cyber attack lasted for almost five years and was named 'Titan Rain,' targeting U.S. defense and government networks in the early 2000s.",
    "Fact: Ransomware attacks have grown by 700% since 2016, with damages projected to cost businesses over $20 billion annually by 2024."
]


def hacking_simulation(num_lines=20, delay=0.3):
    selected_groups = random.sample(all_code_groups, 3)
    code_lines = [line for group in selected_groups for line in group]

    random.shuffle(code_lines)

    for _ in range(num_lines):
        if random.randint(1, 10) == 1:
            random_line = random.choice(code_lines)
            print(random_line)
            fun_fact = random.choice(fun_facts)
            print(Fore.GREEN + fun_fact + "\n")
        else:
            random_line = random.choice(code_lines)
            print(random_line)
        time.sleep(delay)

if __name__ == "__main__":
    hacking_simulation()
    bold = "\033[1m"
    print("")
    print(f"{bold}Completed!")
